from .util import get_shortest_element
from .util import is_empty
from .util import re_fast


def get_single_list(start, length, step):
  """
  获取单个起点的位置端点列表，如果起始位置不是零，则会返回0到起始位置的列表
  Args:
    start: 起始位置
    length: 总长度
    step: 步长
  Examples:
    >>> get_single_list(0, 7, 3) == [[0, 3], [3, 6], [6, 7]]
    >>> get_single_list(1, 7, 3) == [[0, 1], [1, 4], [4, 7]]
  """
  if start > 0:
    res = [[0, start]]
  else:
    res = []
  for i in range(start, length, step):
    if i + step <= length:
      res.append([i, i + step])
    else:
      res.append([i, length])
  return res


def get_breaks(length, step):
  """
  通过长度和步长获所有可能的取端点列表的列表
  Examples:
    >>> get_breaks(10, 3) == [
    >>>   [[0, 3], [3, 6], [6, 9], [9, 10]],
    >>>   [[0, 1], [1, 4], [4, 7], [7, 10]],
    >>>   [[0, 2], [2, 5], [5, 8], [8, 10]]
    >>> ]
  """
  res = []
  for start in range(0, step):
    res.append(get_single_list(start, length, step))
  return res


def get_list_by_position(string: str, breaks: list):
  """
  按照位置信息将字符串拆解为多个字符串的列表
  Args:
    string: 需要拆分的字符串
    breaks: 位置集合列表的列表（左闭右开），[[1, 5], [5, 10], [10, 15]]
  """
  res = []
  for brk in breaks:
    res.append(string[brk[0]:brk[1]])
  return res


def drop_repeat_element(strs: list):
  """删除列表中连续重复的元素"""
  s = ''
  last = ''
  for i in strs:
    if i != last:
      s += i
      last = i
  return s


def drop_repeat_string_by_step(string, step):
  """根据指定的小块长度，获取去重后的字符串"""
  _list = []
  length = len(string)
  for breaks in get_breaks(length, step):
    res = get_list_by_position(string, breaks)
    str_drop = drop_repeat_element(res)
    _list.append(str_drop)

  return get_shortest_element(_list)


def drop_repeat_string(string,
                       min_length=3,
                       max_length=None):
  """
  删除连续重复的字符串，按照step从大到小删除重复字符，返回去重后最短的字符串"""
  if len(string) < min_length * 2:
    return string
  _list = []
  if not max_length:
    max_length = len(string) // 2
  for step in range(max_length, min_length - 1, -1):
    str_drop = drop_repeat_string_by_step(string, step)
    _list.append(str_drop)
    string = get_shortest_element(_list)
  return string


def extract_city(string: str):
  """从字符串中提取城市、区县"""
  from ..resource.city_id import CITI_LIST

  if is_empty(string):
    return
  if not isinstance(string, str):
    return
  for pattern in [
    '(?:自治区|省|新疆|西藏|广西|内蒙古|宁夏)([\\u4e00-\\u9fa5]{2,4}?市)',
    '^([\\u4e00-\\u9fa5]{2,3}?市)',
    '^([\\u4e00-\\u9fa5]{2,3}?[区县])',
  ]:
    if res := re_fast(pattern, string, warning=False):
      return res
  for city in CITI_LIST:
    if city in string:
      return city
