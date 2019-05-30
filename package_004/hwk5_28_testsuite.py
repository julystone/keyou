import unittest
import datetime
from package_004.hwk5_28_testcase import RegisterTestCase
from package_004 import hwk5_28_testcase
import HTMLTestRunnerNew

# 创建一个测试集合
suite = unittest.TestSuite()

# 创建一个执行器
runner = unittest.TextTestRunner()
loader = unittest.TestLoader()

# 添加测试用例
suite.addTest(loader.loadTestsFromTestCase(RegisterTestCase))
# suite.addTest(loader.loadTestsFromModule(hwk5_28_testcase))

i = datetime.datetime.now()
date2display = '{}_{:02}_{:02}_{:02}_{:02}_{:02}'.format(str(i.year)[-2:], i.month, i.day, i.hour, i.minute, i.second)
with open('report_{}.html'.format(date2display), 'wb') as fb:
# with open('report_{}.html'.format('test'), 'wb') as fb:
    test_run = HTMLTestRunnerNew.HTMLTestRunner(stream=fb, verbosity=2, title='py18_%s_report'% date2display, description='参数化报告', tester='july')
    test_run.run(suite)

# runner.run(suite)