import unittest

from package_002.fun2test import register


# 优化上一次的作业
#
# 步骤：
# 1、根据上一次的作业题目的注册函数，写出至少10条用例（写在excel表格中）
# 2、将上次作业的测试用例类参数化，
# 3、创建一个测试集合，读取excel表格中的用例数据，将测试用例全部添加到测试集合中。
# 4、执行测试集合，生成测试报告。


class RegisterTestCase(unittest.TestCase):

    def setUp(self) -> None:
        print('\n' + 'start'.center(32, '-'))

    def tearDown(self) -> None:
        print('end'.center(32, '-'))

    def __init__(self, expected, data, methodName='testRegister'):
        self.expected = expected
        self.data = data
        super().__init__(methodName)

    def testRegister(self):
        actual = register(*self.data)
        try:
            self.assertEqual(self.expected, actual)
        except AssertionError as e:
            print('Not Passed...')
            raise e
        else:
            print('Passed')
