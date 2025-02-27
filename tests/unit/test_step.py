import operator

from sentinel import Step


def test_step_init():
    s = Step("age", operator.add, 100, 100)
    assert isinstance(s, Step)
