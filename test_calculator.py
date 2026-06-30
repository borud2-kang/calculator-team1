import pytest
from calculator import Calc

from calculator import Calc


def test_getGop():

    assert Calc().getGop(2,3) == 6
@pytest.mark.parametrize(
    "a,b,expected",
    [(6, 2, 3), (3, 1, 3)]
)
def test_getDivide(a, b, expected):
    calc = Calc()
    ret = calc.getDivide(a, b)
    assert ret == expected


def test_getDivide_zero_division():
    calc = Calc()
    with pytest.raises(ZeroDivisionError):
        calc.getDivide(2, 0)


@pytest.mark.parametrize(
    "a, b, c, expected",
    [(1, 2, 3, 6), (0, 1, 2, 3)]
)
def test_getSumSum(a, b, c, expected):
    calc = Calc()
    ret = calc.getSumSum(a, b, c)
    assert ret == expected


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
