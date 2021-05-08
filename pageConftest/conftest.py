import pytest

from pageConftest.test_fooObject import Foo

# #conftest中的hook数
def pytest_assertrepr_compare(op,left,right):
    if isinstance(left,Foo) and isinstance(right,Foo) and op ==  '==':
        return ["Comparing Foo isinstance:",f"   vals:{left.val} != {right.val}"]