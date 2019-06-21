import HTMLTestRunnerNew
import time
import unittest

from package_101.common.R_r_config import my_config

path = my_config.get('report', 'path')

# 创建一个测试集合
suite = unittest.TestSuite()

# 创建一个执行器
runner = unittest.TextTestRunner()
loader = unittest.TestLoader()

# 添加测试用例
# suite.addTest(loader.loadTestsFromTestCase(RegisterTestCase))
suite.addTest(loader.discover(r'./testcases'))

date2display = time.strftime('%y_%m_%d_%H_%M_%S', time.localtime())
with open(rf'{path}report_{date2display}.html', 'wb') as fb:
    test_run = HTMLTestRunnerNew.HTMLTestRunner(stream=fb, verbosity=2, title='py18_%s_report' % date2display,
                                                description='参数化报告', tester='july')
    test_run.run(suite)

# runner.run(suite)
