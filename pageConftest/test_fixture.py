import pytest

def dynamic_scope(fixture_name,config):
    if config.getoption("--keep-contain",None):
        return "session"
    return "function"

@pytest.fixture
def first_entry():
    return "a"

@pytest.fixture(scope=dynamic_scope)
def order():
    return []

def test_string(order):
    order.append("b")
    assert order == ["a","c"]

def test_int(order):
    order.append(2)
    assert order == ["a",2]