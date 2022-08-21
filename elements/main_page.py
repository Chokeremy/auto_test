from common.base_page import BasePage
from common.elements_data_utils import ReadElementsData


class MainPage(BasePage):
    """主页面元素操作信息"""

    def __init__(self, driver, sheet_name='main'):
        super().__init__(driver)
        self.elements_info = ReadElementsData(sheet_name).get_elements_info()
        self.my_zone_link = self.elements_info.get('my_zone_link')
        self.user_menu = self.elements_info.get('user_menu')
        self.quit_button = self.elements_info.get('quit_button')

    def move_to_my_zone(self):
        """点击我的地盘"""
        self.element_click(self.my_zone_link)

    def move_to_user_menu(self):
        """点击用户名菜单"""
        self.element_click(self.user_menu)

    def click_quit_button(self):
        """点击退出"""
        self.element_click(self.quit_button)

