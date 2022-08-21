from elements.main_page import MainPage
from elements.login_page import LoginPage


class MainAction:
    """主页面元素操作场景"""

    def __init__(self, driver):
        self.main_page = MainPage(driver)

    def move_zone(self):
        self.main_page.move_to_my_zone()

    def move_menu(self):
        self.main_page.move_to_user_menu()

    def move_quit(self):
        self.main_page.click_quit_button()
        return LoginPage(self.main_page.driver)


