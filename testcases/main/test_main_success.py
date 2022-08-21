import unittest

from actions.main_action import MainAction
from actions.login_action import LoginAction

from common.logs_utils import logger
from common.test_data_utils import ReadTestData
from common.selenium_base_case import SeleniumBaseCase


class TestMainSuccess(SeleniumBaseCase):
    """主页面测试用例"""

    def setUp(self) -> None:
        super().setUp()
        self.test_data = ReadTestData('main').get_test_data_info()

    def test_main_success(self):
        expect_result = self.test_data.get('test_quit_success').get('expect_result')
        logger.info('获取测试数据 - 期望结果: {}'.format(expect_result))
        login_action = LoginAction(self.base_page.driver)
        login_action.default_login()
        main_action = MainAction(self.base_page.driver)
        main_action.move_zone()
        main_action.move_menu()
        login_page = main_action.move_quit()
        actual_result = login_page.get_title()
        self.assertEqual(actual_result.__contains__(expect_result), True)
