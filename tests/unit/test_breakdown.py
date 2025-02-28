import unittest

from sentinelpricing import Breakdown, Step


def test_init_breakdown():
    assert len(Breakdown()) == 1


def test_init_breakdown_with_final_price():
    assert len(Breakdown(final_price=1)) == 1


def test_breakdown_append():
    b = Breakdown()
    b.append("Note")
    assert len(b) == 2


def test_breakdown_repr():
    b = Breakdown()
    assert isinstance(repr(b), str)


def test_breakdown_final_price():
    final_price = 100
    b = Breakdown(final_price)
    assert b.final_price == final_price
