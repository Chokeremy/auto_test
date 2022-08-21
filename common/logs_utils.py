import logging

from common.conf_utils import conf_utils


class LogUtils:
    """设置日志级别和格式"""

    def __init__(self):
        # 创建日志记录器
        self.logger = logging.getLogger()
        # 设置日志级别
        self.logger.setLevel(logging.INFO)
        # 创建文件处理器
        self.file_handler = logging.FileHandler(conf_utils.get_logs_path, 'a', 'utf-8')
        # 创建控制台输出处理器
        self.stream_handler = logging.StreamHandler()
        # 定义日志格式
        self.logs_formatter = logging.Formatter(
            '{} - %(filename)s [line:%(lineno)d - %(levelname)s - %(message)s]'.format(conf_utils.get_datetime))
        # 处理器设置日志格式
        self.file_handler.setFormatter(self.logs_formatter)
        self.stream_handler.setFormatter(self.logs_formatter)
        # 将文件和流处理器添加到日志记录器
        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.stream_handler)

    def get_logger(self):
        # 获取日志记录器
        return self.logger


logger = LogUtils().get_logger()
