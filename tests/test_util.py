from ricco.util import extract_num
from ricco.util import house_type_format
from ricco.util import pinyin
from ricco.util import segment
from ricco.util import to_float


def test_pinyin():
  assert pinyin('测试') == 'ceshi'
  assert pinyin('test') == 'test'


def test_extract_num():
  string = 'fo13--;gr35.3'
  assert extract_num(string) == ['13', '35.3']
  assert extract_num(string, num_type='int') == [13, 35]
  assert extract_num(string, num_type='float') == [13.0, 35.3]
  assert extract_num(string, num_type='str', join_list=True) == '1335.3'


def test_to_float():
  assert to_float('6.5') == 6.5
  assert to_float('6.5%') == 0.065
  assert to_float('6.5%', ignore_pct=True) == 6.5
  assert to_float('p6.5%') == 0.065
  assert to_float('p6.5') == 6.5
  assert to_float('p6.5xx3.5', multi_warning=False) == 5.0
  assert to_float('p6.5xx3.5', rex_method='min', multi_warning=False) == 3.5
  assert to_float('p6.5xx3.5', rex_method='max', multi_warning=False) == 6.5
  assert to_float('p6.5xx3.5', rex_method='sum', multi_warning=False) == 10.0


def test_segment():
  assert segment(55, 20) == '40-60'
  assert segment(55, 20, sep='--', unit='米') == '40--60米'
  assert segment(55, [20]) == '20以上'
  assert segment(10, [20, 50], unit='米') == '20米以下'
  assert segment(20, [20, 50], unit='米') == '20-50米'
  assert segment(50, [20, 50], unit='米') == '50米以上'


def test_house_type_format():
  assert house_type_format('一室一厅') == '1房'
  assert house_type_format('两室一厅') == '2房'
  assert house_type_format('3室两厅') == '3房'
  assert house_type_format('4房1厅') == '4房'
  assert house_type_format('5室1厅') == '5房及以上'
  assert house_type_format('8室1厅') == '5房及以上'
