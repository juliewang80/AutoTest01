import allure
import pytest


# pytest test_allure.py --allure-features=Login -vs -—alluredir=./result1/
# pytest test_allure.py                         -vs --alluredir=./result/
TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'

@allure.feature("Login")
class TestLogin():
    @allure.story("login success")
    @allure.testcase(TEST_CASE_LINK, '测试用例地址')
    def test_login_success(self):
        with allure.step("step1:open"):
            print("open")
        with allure.step("step2:input"):
            print("input")
        print("login success")
        pass

    @allure.story("login fail")
    def test_login_fail(self):
        print("login fail")
        pass

