from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from common.logs_utils import logger
from common.conf_utils import conf_utils


class Browser:
    """根据配置的浏览器类别打开相应的浏览器驱动"""

    def __init__(self):
        self.__driver_category = conf_utils.get_driver_category
        self.__chromedriver_path = conf_utils.get_chromedriver_path
        self.__geckodriver_path = conf_utils.get_geckodriver_path

    def get_driver(self):
        if self.__driver_category == 'chrome':
            return self.__chrome_browser()
        elif self.__driver_category == 'firefox':
            return self.__firefox_browser()
        else:
            logger.warning('浏览器的操作 - 无效的浏览器驱动:{}'.format(self.__driver_category))
            return ''

    def __chrome_browser(self):
        chrome_options = Options()
        # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('--disable-gpu')
        # 设置默认编码为utf-8
        chrome_options.add_argument('lang=zh_CN.UTF-8')
        # 取消chrome受自动控制提示
        chrome_options.add_experimental_option('useAutomationExtension', False)
        # 取消chrome受自动控制提示
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

        logger.info('浏览器的操作 - 打开浏览器驱动:{}'.format(self.__chromedriver_path))
        service = Service(self.__chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver

    def __firefox_browser(self):
        logger.info('浏览器的操作 - 打开浏览器驱动:{}'.format(self.__geckodriver_path))
        service = Service(self.__geckodriver_path)
        driver = webdriver.Firefox(service=service)
        return driver
