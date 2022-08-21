import os
import datetime
import configparser


class ConfUtils:
    """获取各项配置信息"""

    def __init__(self):
        """读取config.ini文件"""

        self.conf_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'conf.ini')
        self.configparser = configparser.ConfigParser()
        self.configparser.read(self.conf_path, encoding='utf-8')

    @property
    def get_url(self):
        """获取config.ini文件中的url地址"""
        return self.configparser.get('default', 'url')

    @property
    def get_driver_category(self):
        """获取config.ini文件中的浏览器类别"""
        return self.configparser.get('default', 'browser')

    @property
    def get_timeout(self):
        """获取config.ini文件中的默认超时及等待时间"""
        return float(self.configparser.get('default', 'timeout'))

    @property
    def get_default_username(self):
        """获取默认用户名"""
        return self.configparser.get('default', 'username')

    @property
    def get_default_password(self):
        """获取默认密码"""
        return self.configparser.get('default', 'password')

    @property
    def get_datetime(self):
        """获取标准时间格式"""
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @property
    def get_cases_path(self):
        """获取所有测试用例的路径"""
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testcases')

    @property
    def get_logs_path(self):
        """获取日志文件的路径"""
        logs_formatter = '{}.log'.format(datetime.datetime.now().strftime('%Y-%m-%d'))
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs', logs_formatter)

    @property
    def get_geckodriver_path(self):
        """获取firefox浏览器驱动的路径"""
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'drivers', 'geckodriver.exe')

    @property
    def get_chromedriver_path(self):
        """获取chrome浏览器驱动的路径"""
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'drivers', 'chromedriver.exe')

    @property
    def get_elements_data_path(self):
        """获取页面元素测试数据excel表格路径"""
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'elements_data', 'element_info_data.xlsx')

    @property
    def get_test_data_path(self):
        """获取测试用例数据excel表格路径"""
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'test_data', 'test_data_info.xlsx')


conf_utils = ConfUtils()
