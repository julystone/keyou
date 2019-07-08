import os
import shutil
import time
import unittest

from package_401.common.R_r_os import REPORT_DIR, DATA_DIR
from package_401.library.HTMLTestRunnerNew import HTMLTestRunner

date2display = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
date2display_cuted = date2display[:10]

# 文件备份
if not os.path.exists(os.path.join(DATA_DIR, f'{date2display_cuted}')):
    shutil.copytree(DATA_DIR, os.path.join(DATA_DIR, f'{date2display_cuted}'))

# 创建一个测试集合
suite = unittest.TestSuite()

# 创建一个执行器
runner = unittest.TextTestRunner()
loader = unittest.TestLoader()

# 添加测试用例
suite.addTest(loader.discover('./testcase', pattern='test_*'))

with open(f'{REPORT_DIR}report_{date2display}.html', 'wb') as fb:
    test_run = HTMLTestRunner(stream=fb, verbosity=2, title='py18_%s_report' % date2display,
                              description='参数化报告', tester='july')
    test_run.run(suite)

# runner.run(suite)
