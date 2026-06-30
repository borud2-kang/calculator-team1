import pytest

from calculator import Calc


def test_sample():
    cal = Calc()
    assert cal.getMinus(10, 5) == 5
    assert cal.getMinus(1, 1) == 0
