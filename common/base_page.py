import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from common.logs_utils import logger
from common.conf_utils import conf_utils


class BasePage:
    """页面公共元素操作方法"""

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)
        logger.info('浏览器的操作 - 打开url地址: {}'.format(url))

    def set_browser_maximize(self):
        self.driver.maximize_window()
        logger.info('浏览器的操作 - 浏览器最大化')

    def set_browser_minimize(self):
        self.driver.minimize_window()
        logger.info('浏览器的操作 - 浏览器最小化')

    @staticmethod
    def sleep(wait_time=conf_utils.get_timeout):
        time.sleep(wait_time)
        logger.info('浏览器的操作 - 固定等待: {}秒钟'.format(wait_time))

    def refresh_browser(self):
        self.driver.refresh()
        logger.info('浏览器的操作 - 刷新浏览器')

    def get_title(self):
        browser_title = self.driver.title
        logger.info('获取基本信息 - 浏览器标题: {}'.format(browser_title))
        return browser_title

    def find_element(self, element_info):
        variable_name = element_info['variable_name']
        locator_type = element_info['locator_type']
        locator_value = element_info['locator_value']
        wait_time = element_info['wait_time']
        if locator_type == 'id':
            locator_type = By.ID
        elif locator_type == 'class':
            locator_type = By.CLASS_NAME
        elif locator_type == 'xpath':
            locator_type = By.XPATH
        elif locator_type == 'css':
            locator_type = By.CSS_SELECTOR
        elif locator_type == 'name':
            locator_type = By.NAME
        else:
            logger.warning('获取测试数据 - 元素定位方式: {}, 无法识别该定位方式'.format(locator_type))
            locator_type = ''

        if locator_type != '':
            element = WebDriverWait(self.driver, wait_time).until(lambda x: x.find_element(locator_type, locator_value))
        else:
            element = ''

        logger.info('获取测试数据 - 页面名称: {}; 页面元素定位方式: {}; 页面元素定位取值: {}; 元素操作后等待时间: {}'.
                    format(variable_name, locator_type, locator_value, wait_time))
        return element, variable_name, locator_type, locator_value, wait_time

    def element_click(self, element_info):
        element, variable_name, locator_type, locator_value, wait_time = self.find_element(element_info)
        element.click()
        logger.info('执行元素操作 - 点击元素 - 页面元素定位方式: {}; 页面元素定位取值: {}'.format(locator_type, locator_value))
        self.sleep(wait_time)

    def element_input(self, element_info, send_content):
        element, locator_name, locator_type, locator_value, wait_time = self.find_element(element_info)
        element.send_keys(send_content)
        logger.info('执行元素操作 - 输入文本 - 页面元素定位方式: {}; 页面元素定位取值: {}; 页面元素输入文本: {}'.
                    format(locator_type, locator_value, send_content))
        self.sleep(wait_time)

    def switch_to_alert(self, action='accept', wait_time=conf_utils.get_timeout):
        WebDriverWait(self.driver, wait_time).until(ec.alert_is_present())
        alert = self.driver.switch_to.alert
        if action == 'accept':
            alert.accept()
        else:
            alert.dismiss()
        return alert.text

    def quit_browser(self):
        self.driver.quit()
        logger.info('浏览器的操作 - 退出浏览器')
