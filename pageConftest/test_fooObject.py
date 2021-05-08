import pytest

class Foo:
    def __init__(self,val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val

@pytest.fixture
def error_fixture():
    assert 0

def test_foo():
    f1 = Foo(1)
    f2 = Foo(3)
    assert f1 == f2

def test_pass():
    assert 1

def test_fail():
    assert 0

def test_OK():
    print("ok")

def test_error(error_fixture):
    pass

def test_skip():
    pytest.skip("skip")

def test_xfail():
    pytest.xfail("xfail")




@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    assert 1
