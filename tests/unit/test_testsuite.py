from sentinel import TestCase
from sentinel import TestSuite


def test_testsuite_init():
    testcases = [TestCase({"age": i + 17, "lic": i + 17}) for i in range(25)]

    ts = TestSuite(testcases)

    assert isinstance(ts, TestSuite)


def test_testsuite_get():
    testcases = [TestCase({"age": i + 17, "lic": i + 17}) for i in range(25)]

    ts = TestSuite(testcases)

    ts.testcases.insert(15, TestCase({"age": 0, "lic": 18}))

    assert ts[15]["age"] == 0


def test_testsuite_add():
    LEN = 5
    testcases = [TestCase({"age": i + 17}) for i in range(LEN)]
    other_testcases = [TestCase({"lic": i + 17}) for i in range(LEN)]

    ts = TestSuite(testcases)
    other_ts = TestSuite(other_testcases)

    combined = ts + other_ts

    assert isinstance(combined, TestSuite)
    assert len(combined) == LEN * 2
    print(combined[0])
    print("age" in combined[0])
    assert "age" in combined[0]
    assert "age" not in combined[5]
    assert "lic" not in combined[0]
    assert "lic" in combined[5]
