import pytest

from calculator import Calc

@pytest.mark.parametrize(
    "a,b,expected",
    [(6,2,3),(3,1,3)]
)
def test_getDivide(a, b, expected):
    calc = Calc()
    ret = calc.getDivide(a, b)
    assert ret == expected


def test_getDivide_zero_division():
    calc = Calc()
    with pytest.raises(ZeroDivisionError):
        calc.getDivide(2, 0)

