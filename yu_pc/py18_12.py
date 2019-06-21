# -*-coding:utf8-*-
'''
============================
author:guxiangyu
time:2019/5/20
E-mail:317096158@qq.com
============================
'''
import unittest

from py18_01.register import register


class RegisterTestCase(unittest.TestCase):
    def __init__(self, methodName, expected, data):
        self.expected = expected
        self.data = data
        super.__init__(methodName)

    def setUp(self):
        print('执行每一条用例之前都会执行这个方法，做测试之前的环境准备')

    def tearDown(self):
        print('每一条用例执行完都会执行，可以用来恢复环境')

    # 一个用例就是一个方法，方法名必须要以test开头
    def test_register(self):
        # 帐号密码都正确
        # 预期结果
        res = register(*self.data)
        try:
            self.assertEqual(self.expected, res)
        except AssertionError as e:
            print('该条测试用例未通过')
            raise e
        else:
            print('pass')

    def test_username_exist(self):
        expected = {"code": 0, "msg": "该账户已存在"}
        data = ('python18', '123456', '123456')
        res = register(*data)
        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            print('该条测试用例未通过')
            raise e
        else:
            print('pass')

    def test_password_error(self):
        expected = {"code": 0, "msg": "两次密码不一致"}
        data = ('python19', '123456', '1234567')
        res = register(*data)
        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            print('该条测试用例未通过')
            raise e
        else:
            print('pass')

    def test_username_lengtherror(self):
        expected = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        data = ('pytho', '123456', '123456')
        res = register(*data)
        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            print('该条测试用例未通过')
            raise e
        else:
            print('pass')

    def test_password_lengtherror(self):
        expected = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        data = ('python', '12345', '12345')
        res = register(*data)
        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            print('该条测试用例未通过')
            raise e
        else:
            print('pass')


if __name__ == '__main__':
    unittest.main()
