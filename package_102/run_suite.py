import HTMLTestRunnerNew
import time
import unittest
from package_102.common.R_r_os import my_os

report_path = my_os.readpath('report')

# 创建一个测试集合
suite = unittest.TestSuite()

# 创建一个执行器
runner = unittest.TextTestRunner()
loader = unittest.TestLoader()

# 添加测试用例
suite.addTest(loader.discover("./testcase"))

date2display = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
with open(f'{report_path}report_{date2display}.html', 'wb') as fb:
    test_run = HTMLTestRunnerNew.HTMLTestRunner(stream=fb, verbosity=2, title='py18_%s_report' % date2display,
                                                description='参数化报告', tester='july')
    test_run.run(suite)

# runner.run(suite)
