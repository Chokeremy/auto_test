import xlrd

from common.conf_utils import conf_utils


class ReadTestData:
    """读取测试用例测试数据"""

    def __init__(self, sheet_name):
        self.workbook = xlrd.open_workbook(conf_utils.get_test_data_path)
        self.sheet = self.workbook.sheet_by_name(sheet_name)
        self.row_count = self.sheet.nrows
        self.column_count = self.sheet.ncols

    def get_test_data_info(self):
        test_data_info = {}
        for i in range(1, self.row_count):
            data_info = {'test_class_name': self.sheet.cell_value(i, 2), 'expect_result': self.sheet.cell_value(i, 4),
                         'test_parameter': []}
            for j in range(5, self.column_count):
                if len(self.sheet.cell_value(i, j)) >= 3 and self.sheet.cell_value(i, j).__contains__('='):
                    test_param_list = self.sheet.cell_value(i, j).split('=')
                    data_info['test_parameter'].append({test_param_list[0]: test_param_list[1]})
            test_data_info[self.sheet.cell_value(i, 0)] = data_info

        return test_data_info
