import unittest

from ddt import ddt, data

from package_004.R_r_excel import ReadExcel
from package_004.fun2test import register

# 优化上一次的作业
#
# 步骤：
# 1、根据上一次的作业题目的注册函数，写出至少10条用例（写在excel表格中）
# 2、将上次作业的测试用例类参数化，
# 3、创建一个测试集合，读取excel表格中的用例数据，将测试用例全部添加到测试集合中。
# 4、执行测试集合，生成测试报告。

wb = ReadExcel('cases.xlsx', 'Sheet1')
# cases = wb.r_data_obj_from_column([1, 2, 4])
cases = wb.read_data_obj()
print(cases)


@ddt
class RegisterTestCase(unittest.TestCase):

    def setUp(self) -> None:
        print('\n' + 'start'.center(32, '-'))

    def tearDown(self) -> None:
        print('end'.center(32, '-'))

    @data(*cases)
    def testRegister(self, case):
        actual = register(*eval(case.data))
        try:
            self.assertEqual(eval(case.expected), actual)
        except AssertionError as e:
            print('Not Passed...')
            result = 'failed'
            raise e
        else:
            print('Passed')
            result = 'passed'
        finally:
            wb.write_data(case.case_id + 1, 6, result)
