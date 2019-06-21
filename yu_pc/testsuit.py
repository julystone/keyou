# -*-coding:utf8-*-
'''
============================
author:guxiangyu
time:2019/5/26
E-mail:317096158@qq.com
============================
'''
# 创建测试集合
import unittest

from py18_01.py18_12 import RegisterTestCase
from py18_01.py18_hw0526 import ReadExcel

suite = unittest.TestSuite()

# 读取excel中数据

r = ReadExcel('cases.xlsx', 'Sheet')
cases = r.read_data_obj([2, 3])
for case in cases:
    # 用例遍历出来
    suite.addTest(RegisterTestCase('test_register', eval(case.expected), eval(case.data)))

# # 第一种：单个用例添加
# suite.addTest(RegisterTestCase('test_register'))
# suite.addTest(RegisterTestCase('test_username_exist'))
# suite.addTest(RegisterTestCase('test_password_error'))
# suite.addTest(RegisterTestCase('test_username_lengtherror'))
# suite.addTest(RegisterTestCase('test_password_lengtherror'))
# 第二种：一次添加用例类
# loader = unittest.TestLoader()
# suite.addTest(RegisterTestCase('test_register',case['expected'],))

# 执行用例
# with open('report.html','wb')as f :
#     runner = HTMLTestRunner(stream=f,verbosity=2,title='py18_report',description='第一份测试报告',tester='Gxy')
#     runner.run(suite)
