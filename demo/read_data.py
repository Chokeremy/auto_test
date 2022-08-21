import xlrd

from common.conf_utils import conf_utils


class ReadElementsData:
    """读取页面操作测试数据"""

    def __init__(self):
        self.workbook = xlrd.open_workbook(conf_utils.get_elements_data_path)
        # self.sheet = self.workbook.sheet_by_name()
        self.sheet_name = self.workbook.sheet_names()

    def get_sheet_data(self):
        if self.sheet_name == 'login':
            return self.sheet_name
        else:
            return self.sheet_name


r = ReadElementsData().get_sheet_data()
print(r)

