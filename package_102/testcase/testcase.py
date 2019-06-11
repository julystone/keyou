from package_102.fun2test import register
from package_102.common.R_r_excel import ReadExcel
from package_102.common.R_r_config import my_config
from package_102.common.R_r_log import my_log
from package_102.common.R_r_os import DATA_DIR
import unittest
from ddt import ddt, data

# 优化上一次的作业
#
# 步骤：
# 1、根据上一次的作业题目的注册函数，写出至少10条用例（写在excel表格中）
# 2、将上次作业的测试用例类参数化，
# 3、创建一个测试集合，读取excel表格中的用例数据，将测试用例全部添加到测试集合中。
# 4、执行测试集合，生成测试报告。

excel_path = DATA_DIR
file_name = my_config.get('excel', 'file_name')
sheet_name = my_config.get('excel', 'sheet_name')
columns_read = my_config.get('excel', 'columns_read')


wb = ReadExcel(f'{excel_path}{file_name}', sheet_name)
cases = wb.r_data_obj_from_column(eval(columns_read))
# cases = wb.read_data_obj()
print(cases)


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
            wb.w_save()
            my_log.info(f'TestCase {case.case_name} end')