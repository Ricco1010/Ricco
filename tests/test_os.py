from ricco.util.os import ext
from ricco.util.os import fn


def test_fn():
  assert fn('test_util.py') == 'test_util'


def test_ext():
  assert ext('test_util.py') == '.py'