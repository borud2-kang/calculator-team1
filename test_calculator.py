import pytest
from calculator import Calc

from calculator import Calc


def test_getGop():

    assert Calc().getGop(2,3) == 6
def test_sample():
    cal = Calc()
    assert cal.getMinus(10, 5) == 5
    assert cal.getMinus(1, 1) == 0
    
@pytest.mark.parametrize("a,b,expected", [(1,2,3),(4,5,9)])
def test_get_sum(a,b,expected):
    calc = Calc()
    assert expected == calc.getSum(a, b)

def test_getZegop():
    cal = Calc()

    result = cal.getZegop(2)

    assert result == 4
