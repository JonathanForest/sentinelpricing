from sentinel.models.rate import Rate


def test_rate_equality():
    rate1 = Rate(name="age", value=100)
    rate2 = Rate(name="age", value=100)
    rate3 = Rate(name="age", value=200)
    rate4 = Rate(name="lic", value=200)

    assert rate1 == rate2
    assert rate2 != rate3
    assert rate3 == rate4


def test_rate__add__():
    rate1 = Rate(name="age", value=100)
    rate2 = Rate(name="age", value=100)

    assert rate1 + rate2 == 200
    assert rate1 + 100 == 200


def test_rate__sub__():
    rate1 = Rate(name="age", value=100)
    rate2 = Rate(name="age", value=100)

    assert rate1 - rate2 == 0
    assert rate1 - 100 == 0


def test_rate__mul__():
    rate1 = Rate(name="age", value=100)
    rate2 = Rate(name="age", value=2)

    assert rate1 * rate2 == 200
    assert rate1 * 2 == 200


def test_rate__truediv__():
    rate1 = Rate(name="age", value=7)
    rate2 = Rate(name="age", value=2)

    assert rate1 / rate2 == 3.5
    assert rate1 / 2 == 3.5


def test_rate__floordiv__():
    rate1 = Rate(name="age", value=7)
    rate2 = Rate(name="age", value=2)

    assert rate1 // rate2 == 3
    assert rate1 // 2 == 3
