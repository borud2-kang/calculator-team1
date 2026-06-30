import pytest

from calculator import Calc


def test_sample():
    assert 1 == 1
    pytest.fail()

def test_getGop():

    assert Calc().getGop(2,3) == 6