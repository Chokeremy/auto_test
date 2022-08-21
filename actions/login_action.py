from common.logs_utils import logger
from common.conf_utils import conf_utils
from elements.login_page import LoginPage


class LoginAction:
    """登录页面元素操作场景"""

    def __init__(self, driver):
        self.login_page = LoginPage(driver)

    def login_action(self, username, password):
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.button_click()

    def default_login(self):
        self.login_action(conf_utils.get_default_username, conf_utils.get_default_password)

    def login_success(self, username, password):
        self.login_action(username, password)

    def login_failure(self, username, password):
        self.login_action(username, password)
        logger.error(self.login_page.switch_to_alert())
