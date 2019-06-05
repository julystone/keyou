from package_101.fun2test import register
from package_101.common.R_r_excel import ReadExcel
from package_101.common.R_r_config import my_config
from package_101.common.R_r_log import my_log
import unittest
from ddt import ddt, data


sheet_name = my_config.get('excel', 'sheet_name')
columns_read = my_config.get('excel', 'columns_read')
path = my_config.get('excel', 'path')


wb = ReadExcel(f'{path}cases.xlsx', sheet_name)

if eval(columns_read) == []:
    cases = wb.r_data_obj()
else:
    cases = wb.r_data_obj_from_column(eval(columns_read))


@ddt
class RegisterTestCase(unittest.TestCase):

    def setUp(self) -> None:
        print('\n'+'start'.center(32, '-'))

    def tearDown(self) -> None:
        print('end'.center(32, '-'))

    @data(*cases)
    def testRegister(self, case):
        actual = register(*eval(case.data))
        my_log.info(f'TestCase {case.case_name} starting------')
        try:
            self.assertEqual(eval(case.expected), actual)
        except AssertionError as e:
            print('Not Passed...')
            result = 'failed'
            my_log.error(f'【Failed】：E{case.expected} != A{actual}')
            raise e
        else:
            print('Passed')
            result = 'passed'
            my_log.info(f'【Success】')
        finally:
            wb.w_data(case.case_id + 1, 6, result)
            my_log.info(f'TestCase {case.case_name} end')