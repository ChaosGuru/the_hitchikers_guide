from hitchikers.scripts import concatstring


def test_concat():
    assert concatstring.concat(3) == '012'


def test_with_join():
    assert concatstring.with_join(3) == '012'


def test_with_comprehension():
    assert concatstring.with_comprehension(3) == '012'