from common.base_page import BasePage
from common.elements_data_utils import ReadElementsData


class LoginPage(BasePage):
    """登录页面元素操作信息"""

    def __init__(self, driver, sheet_name='login'):
        super().__init__(driver)
        self.elements_info = ReadElementsData(sheet_name).get_elements_info()
        self.input_user = self.elements_info.get('input_username')
        self.input_pwd = self.elements_info.get('input_password')
        self.login_button = self.elements_info.get('login_button')

    def input_username(self, content):
        self.element_input(self.input_user, content)

    def input_password(self, content):
        self.element_input(self.input_pwd, content)

    def button_click(self):
        self.element_click(self.login_button)

    def get_alert_msg(self):
        return self.switch_to_alert()
