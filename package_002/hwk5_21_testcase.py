from package_002.fun2test import register
import unittest

# 对下面功能函数  设计用例进行单元测试，
#
# 要求
# 1、 设计至少五条用例
#
# 2、至少用两种方式往测试集合中添加测试用例
#
# 3、执行测试集合中的测试用例


class RegisterTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print('start'.center(32, '-'))

    def tearDown(self) -> None:
        print('end'.center(32, '-'))

    def testRegister(self):
        # users = [{'username': 'python18', 'password1': '123456', 'password2':'123456'}]
        users = ['july401', '123456', '123456']
        expected = {"code": 1, "msg": "注册成功"}
        actual = register(*users)
        try:
            self.assertEqual(expected, actual)
        except AssertionError as e:
            print('Not Passed...')
            raise e
        else:
            print('Passed')

    def test_Multiusername(self):
        users = ['python18', '123456', '123456']
        expected = {'code': 0, 'msg': '该账户已存在'}
        actual = register(*users)
        try:
            self.assertEqual(expected, actual)
        except AssertionError as e:
            print('Not Passed...')
            raise e
        else:
            print('Passed')

    def test_DiffPass(self):
        users = ['muyu18', '123456', '1234567']
        expected = {"code": 0, "msg": "两次密码不一致"}
        actual = register(*users)
        try:
            self.assertEqual(expected, actual)
        except AssertionError as e:
            print('Not Passed...')
            raise e
        else:
            print('Passed')

    def test_LenOfUserIllegal(self):
        users = ['muyu', '123456', '123456']
        expected = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        actual = register(*users)
        try:
            self.assertEqual(expected, actual)
        except AssertionError as e:
            print('Not Passed...')
            raise e
        else:
            print('Passed')
    def test_LenOfPassIllegal(self):
        users = ['muyu18', '1234', '1234']
        expected = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        actual = register(*users)
        try:
            self.assertEqual(expected, actual)
        except AssertionError as e:
            print('Not Passed...')
            raise e
        else:
            print('Passed')


    