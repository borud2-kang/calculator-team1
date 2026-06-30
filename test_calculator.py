import pytest
from calculator import Calc

def test_sample():
    assert 1 == 1
    pytest.fail()

def test_getZegop():
    cal = Calc()

    result = cal.getZegop(2)

    assert result == 4
