import unittest

from actions.login_action import LoginAction

from common.test_data_utils import ReadTestData
from common.selenium_base_case import SeleniumBaseCase


class TestLoginSuccess(SeleniumBaseCase):
    """登录成功测试用例"""

    def setUp(self) -> None:
        super().setUp()
        self.test_data = ReadTestData('login').get_test_data_info()

    def test_login_success(self):
        test_params = self.test_data.get('test_login_success').get('test_parameter')
        username = test_params[0].get('username')
        password = test_params[1].get('password')
        login_action = LoginAction(self.base_page.driver)
        login_action.login_success(username, password)
