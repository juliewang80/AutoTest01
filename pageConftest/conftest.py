import pytest

from pageConftest.test_fooObject import Foo


# #conftest中的hook数
def pytest_assertrepr_compare(op, left, right):
    """

    :rtype: object
    """
    if isinstance(left, Foo) and isinstance(right, Foo) and op == '==':
        return ["Comparing Foo isinstance:", f"   vals:{left.val} != {right.val}"]

# @pytest.fixture(scope="function",autouse=True)
# def append_order(order,first_entry,config):
#     return order.append(first_entry)


@pytest.fixture
def conf_002():
    print("conf_002")
    return "34"