import HTMLTestRunnerNew
import datetime
import unittest

import openpyxl

from package_003.hwk5_23_testcase import RegisterTestCase

# 创建一个测试集合
suite = unittest.TestSuite()

# 创建一个执行器
runner = unittest.TextTestRunner()
loader = unittest.TestLoader()
# 添加测试用例

wb = openpyxl.load_workbook('test_file.xlsx')
sh = wb['Sheet1']
for case in list(sh.rows)[1:]:
    case_id = case[0].value
    case_expected = eval(case[1].value)
    case_data = eval(case[2].value)
    # suite.addTest(loader.loadTestsFromTestCase(RegisterTestCase(case_expected, case_data)))
    suite.addTest(RegisterTestCase(case_expected, case_data))

i = datetime.datetime.now()
date2display = '{}_{:02}_{:02}_{:02}_{:02}_{:02}'.format(str(i.year)[-2:], i.month, i.day, i.hour, i.minute, i.second)
with open('report_{}.html'.format(date2display), 'wb') as fb:
    test_run = HTMLTestRunnerNew.HTMLTestRunner(stream=fb, verbosity=2, title='py18_%s_report' % date2display,
                                                description='参数化报告', tester='july')
    test_run.run(suite)

# runner.run(suite)
