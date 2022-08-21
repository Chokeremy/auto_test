import xlrd
from common.conf_utils import conf_utils


class ReadElementsData:
    """读取页面操作测试数据"""

    def __init__(self, sheet_name):
        self.workbook = xlrd.open_workbook(conf_utils.get_elements_data_path)
        self.sheet = self.workbook.sheet_by_name(sheet_name)
        self.row_count = self.sheet.nrows

    def get_elements_info(self):
        elements_info = {}
        for i in range(1, self.row_count):
            element_info = {'variable_name': self.sheet.cell_value(i, 0),
                            'locator_type': self.sheet.cell_value(i, 3), 'locator_value': self.sheet.cell_value(i, 4)}

            wait_time = self.sheet.cell_value(i, 5)
            wait_time = wait_time if isinstance(wait_time, float) else conf_utils.get_timeout
            element_info['wait_time'] = wait_time
            elements_info[self.sheet.cell_value(i, 1)] = element_info

        return elements_info
