import unittest

from common.browser import Browser
from common.logs_utils import logger
from common.base_page import BasePage
from common.conf_utils import conf_utils


class SeleniumBaseCase(unittest.TestCase):
    """测试用例公共部分初始化和结束"""

    @classmethod
    def setUpClass(cls) -> None:
        logger.info('浏览器的操作 - 测试用例类初始化')

    def setUp(self) -> None:
        self.base_page = BasePage(Browser().get_driver())
        self.base_page.open_url(conf_utils.get_url)
        self.base_page.set_browser_maximize()

    def tearDown(self) -> None:
        self.base_page.quit_browser()

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info('浏览器的操作 - 测试用例类执行完成')

