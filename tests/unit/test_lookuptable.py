import unittest

from sentinelpricing import LookupTable, Rate


def test_lookuptable_init():
    rates = [{"age": i, "rate": i * 5} for i in range(0, 100, 5)]

    lookuptable = LookupTable(rates)

    assert lookuptable.lookup(0) == 0
    assert lookuptable.lookup(50) == 50 * 5
    assert lookuptable.lookup(53) == 50 * 5
    assert lookuptable.lookup(55) == 55 * 5


def test_lookuptable_index_col():
    rates = [{"age": i, "rate": i * 5} for i in range(0, 100, 5)]

    lookuptable = LookupTable(rates)

    assert isinstance(lookuptable.index, list)


def test_lookuptable_rate_col():
    rates = [{"age": i, "rate": i * 5} for i in range(0, 100, 5)]

    lookuptable = LookupTable(rates)

    assert isinstance(lookuptable.rates, list)
