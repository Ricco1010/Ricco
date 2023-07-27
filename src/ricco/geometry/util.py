import json
import warnings

import geojson
import numpy as np
import pandas as pd
from shapely import wkb
from shapely import wkt
from shapely.errors import GeometryTypeError
from shapely.errors import ShapelyDeprecationWarning
from shapely.errors import WKBReadingError
from shapely.geometry import MultiLineString
from shapely.geometry import MultiPolygon
from shapely.geometry import Point
from shapely.geometry import Polygon
from shapely.geometry import shape
from shapely.geos import WKTReadingError

from ..util.util import ensure_list
from ..util.util import is_empty
from ..util.util import not_empty

warnings.filterwarnings('ignore', category=ShapelyDeprecationWarning)


class GeomFormat:
  wkb = 'wkb'
  wkt = 'wkt'
  shapely = 'shapely'
  geojson = 'geojson'
  unknown = 'unknown'


def crs_sh2000():
  """测绘院（上海2000）crs信息"""
  from ..resource.crs import CRS_SH2000
  return CRS_SH2000


def get_epsg_by_lng(lng):
  """通过经度获取epsg代码"""
  lng_epsg_mapping = {
    # 中央经线和epsg代码的对应关系
    75: 4534, 78: 4535, 81: 4536, 84: 4537, 87: 4538,
    90: 4539, 93: 4540, 96: 4541, 99: 4542,
    102: 4543, 105: 4544, 108: 4545, 111: 4546,
    114: 4547, 117: 4548, 120: 4549, 123: 4550,
    126: 4551, 129: 4552, 132: 4553, 135: 4554,
  }
  lng = ensure_list(lng)
  lng = [i for i in lng if not_empty(i)]
  lng = np.median(lng)
  key = min(lng_epsg_mapping.keys(), key=lambda x: abs(x - lng))
  return lng_epsg_mapping.get(key)


def get_lng_by_city(city: str):
  from ..resource.epsg_code import CITY_POINT
  if city in CITY_POINT.keys():
    return CITY_POINT[city]['lng']
  else:
    city += '市'
    if city in CITY_POINT.keys():
      return CITY_POINT[city]['lng']
    else:
      warnings.warn(f'请补充{city}的epsg信息，默认返回经度120')
      return 120


def get_epsg(city: str):
  """根据城市查询epsg代码，用于投影"""
  return get_epsg_by_lng(get_lng_by_city(city))


def projection_lnglat(lnglat, crs_from, crs_to):
  from pyproj import Transformer
  transformer = Transformer.from_crs(crs_from, crs_to)
  return transformer.transform(xx=lnglat[1], yy=lnglat[0])


def wkb_loads(x, hex=True):
  warnings.filterwarnings('ignore',
                          'Geometry column does not contain geometry.',
                          UserWarning)

  if is_empty(x):
    return

  try:
    return wkb.loads(x, hex=hex)
  except (AttributeError, WKBReadingError) as e:
    warnings.warn(f'{e}, 【{x}】')
    return


def wkb_dumps(x, hex=True, srid=4326) -> (str, None):
  if is_empty(x):
    return

  try:
    return wkb.dumps(x, hex=hex, srid=srid)
  except AttributeError as e:
    warnings.warn(f'{e}, 【{x}】')
    return


def wkt_loads(x):
  if is_empty(x):
    return
  try:
    return wkt.loads(x)
  except (AttributeError, WKTReadingError, TypeError) as e:
    warnings.warn(f'{e}, 【{x}】')
    return


def wkt_dumps(x) -> (str, None):
  if is_empty(x):
    return
  try:
    return wkt.dumps(x)
  except AttributeError as e:
    warnings.warn(f'{e}, 【{x}】')
    return


def geojson_loads(x):
  """geojson文本形式转为shapely格式"""
  from simplejson.errors import JSONDecodeError

  if is_empty(x):
    return
  try:
    geom = shape(geojson.loads(x))
    if geom.is_empty:
      return
    return geom
  except (JSONDecodeError, AttributeError, GeometryTypeError, TypeError) as e:
    warnings.warn(f'{e}, 【{x}】')
    return


def geojson_dumps(x) -> (str, None):
  """shapely转为geojson文本格式"""
  if is_empty(x):
    return
  try:
    geom = geojson.Feature(geometry=x)
    return json.dumps(geom.geometry)
  except TypeError as e:
    warnings.warn(f'{e}, 【{x}】')
    return


def is_shapely(x, na=False) -> bool:
  """判断是否为shapely格式"""
  from ..resource.geometry import GeomTypeSet
  if pd.isna(x):
    return na
  if type(x) in GeomTypeSet:
    return True
  else:
    return False


def is_wkb(x, na=False) -> bool:
  """判断是否为wkb格式"""
  if not isinstance(x, str):
    return False
  if pd.isna(x):
    return na
  try:
    wkb.loads(x, hex=True)
    return True
  except WKBReadingError:
    return False


def is_wkt(x, na=False) -> bool:
  """判断是否为wkt格式"""
  if not isinstance(x, str):
    return False
  if pd.isna(x):
    return na
  try:
    wkt.loads(x)
    return True
  except WKTReadingError:
    return False


def is_geojson(x, na=False) -> bool:
  """判断是否为geojson格式"""
  from simplejson.errors import JSONDecodeError

  if not isinstance(x, (str, dict)):
    return False
  if pd.isna(x):
    return na
  try:
    if shape(geojson.loads(x)).is_empty:
      return False
    return True
  except (JSONDecodeError, AttributeError, GeometryTypeError, TypeError):
    return False


def infer_geom_format(x):
  """推断geometry格式"""
  if is_shapely(x):
    return GeomFormat.shapely
  if is_wkb(x):
    return GeomFormat.wkb
  if is_wkt(x):
    return GeomFormat.wkt
  if is_geojson(x):
    return GeomFormat.geojson
  return GeomFormat.unknown


def ensure_multi_geom(geom):
  """将LineString和Polygon转为multi格式"""
  if geom.geom_type == 'LineString':
    return MultiLineString([geom])
  if geom.geom_type == 'Polygon':
    return MultiPolygon([geom])
  return geom


def multiline2multipolygon(multiline_shapely):
  """multiline转为multipolygon，直接首尾相连"""
  coords = []
  for line in multiline_shapely:
    lngs = line.xy[0]
    lats = line.xy[1]
    for i in range(len(lngs)):
      lng, lat = lngs[i], lats[i]
      point = Point((lng, lat))
      if len(coords) >= 1:
        if point != coords[-1]:
          coords.append(point)
      else:
        coords.append(point)
  try:
    return MultiPolygon([Polygon(coords)])
  except ValueError as e:
    warnings.warn(f'{e}，{multiline_shapely}')
    return


def get_inner_point(polygon: Polygon, within=True):
  """返回面内的一个点，默认返回中心点，当中心点不在面内则返回面内一个点"""
  if is_empty(polygon):
    return
  point = polygon.centroid
  if not polygon.is_valid:
    polygon = polygon.buffer(0.000001)
  if polygon.contains(point) or not within:
    return point
  return polygon.representative_point()


def ensure_lnglat(lnglat) -> tuple:
  if isinstance(lnglat, (list, tuple)):
    if all([isinstance(i, (float, int)) for i in lnglat]):
      return lnglat
    else:
      raise TypeError('数据类型错误，经度和纬度都应该为数值型')
  if is_shapely(lnglat):
    geom = lnglat
  elif is_wkt(lnglat):
    geom = wkt_loads(lnglat)
  elif is_wkb(lnglat):
    geom = wkb_loads(lnglat)
  elif is_geojson(lnglat):
    geom = geojson_loads(lnglat)
  else:
    raise ValueError('未知的地理类型')
  return (geom.x, geom.y)


def distance(
    p1: (tuple, str),
    p2: (tuple, str),
    city: str = None,
    epsg_from: int = 4326,
    epsg_to: (str, int) = None):
  """
  计算两个点（经度，纬度）之间的距离，单位：米
  Args:
    p1: 点位1，经纬度或geometry
    p2: 点位2，经纬度或geometry
    city: 所在城市，用于投影
    epsg_from: epsg代码
    epsg_to: 投影epsg代码
  """
  p1, p2 = ensure_lnglat(p1), ensure_lnglat(p2)
  if not epsg_to:
    epsg_to = get_epsg(city) if city else get_epsg_by_lng([p1[0], p2[0]])
  p1 = projection_lnglat(p1, epsg_from, epsg_to)
  p2 = projection_lnglat(p2, epsg_from, epsg_to)
  return Point(p1).distance(Point(p2))