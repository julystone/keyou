import datetime
import unittest

from package_002 import hwk5_21_testcase
from package_002.hwk5_21_testcase import RegisterTestCase

# 创建一个测试集合
suite = unittest.TestSuite()

# 创建一个执行器
runner = unittest.TextTestRunner()

# 添加测试用例
# 1
suite.addTest(RegisterTestCase('test_Multiusername'))
suite.addTest(RegisterTestCase('test_DiffPass'))
# 2
suite.addTests([RegisterTestCase('test_Multiusername'), RegisterTestCase('test_DiffPass')])
# 3
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(RegisterTestCase))
# 4
suite.addTest(loader.loadTestsFromModule(hwk5_21_testcase))

j = datetime.datetime.today()
i = datetime.datetime.now()
date2display = '{:.2}_{:02}_{:02}_{:02}_{:02}_{:02}'.format('aabbcc', i.month, i.day, i.hour, i.minute, i.second)
print("yy".format(i))
print(j)
print(date2display)
# with open('report_{}.html'.format(date2display), 'wb') as fb:
#
#     test_run = HTMLTestRunnerNew.HTMLTestRunner(stream=fb, verbosity=2, title='py18_%s_report'%date2display, description='july', tester='july')
#     test_run.run(suite)


# runner.run(suite)
