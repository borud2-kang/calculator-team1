import pytest
from calculator import *


def test_sample():
    assert 1 == 1
    pytest.fail()

@pytest.mark.parametrize("a,b,expected", [(1,2,3),(4,5,9)])
def test_get_sum(a,b,expected):
    calc = Calc(a, b)
    assert expected == calc.getSum()

