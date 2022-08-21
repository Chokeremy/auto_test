import unittest
from common.conf_utils import conf_utils

if __name__ == '__main__':
    """执行器"""

    discover_cases = unittest.defaultTestLoader.discover(conf_utils.get_cases_path, 'test*.py')
    all_suite = unittest.TestSuite()
    all_suite.addTests(discover_cases)

    unittest.main(defaultTest='all_suite')
