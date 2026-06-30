import pytest

from calculator import Calc


def test_getGop():

    assert Calc().getGop(2,3) == 6