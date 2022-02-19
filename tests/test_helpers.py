from emptycabinet.dep import helpers


def test_helpers():
    assert helpers.add(2, 2) == 4
    assert helpers.add(1, 2) != 4
