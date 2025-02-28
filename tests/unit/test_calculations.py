from sentinelpricing.utils.calculations import dict_difference, dict_transpose


def test_dict_subtract():
    a = {"a": 30, "b": 10}
    b = {"a": 20, "c": 5}
    expected = {"a": -10, "b": -10, "c": 5}
    assert dict_difference(a, b) == expected


def test_dict_transpose():
    a = {"a": {"z": 1, "y": 2}, "b": {"z": 3, "y": 4}}

    expected_result = {
        "z": {"a": 1, "b": 3},
        "y": {"a": 2, "b": 4},
    }

    assert dict_transpose(a) == expected_result
