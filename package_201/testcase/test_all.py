import json
import unittest

from package_201.common.R_r_config import my_config
from package_201.common.R_r_excel import ReadExcel
from package_201.common.R_r_log import my_log
from package_201.common.R_r_os import DATA_DIR, CONF_DIR
from package_201.common.R_r_sql import Mysql
from package_201.common.R_request import HttpRequestNoCookie, HttpRequest
from package_201.common.generate import my_generate
from package_201.library.ddt import ddt, data

file_name = my_config.get('excel', 'file_name')
file_path = f'{DATA_DIR}{file_name}'
yaml_file = f'{CONF_DIR}parms.yaml'
# sheet_name = 'login'

testRequestNoCookie = HttpRequestNoCookie()
testRequest = HttpRequest()


@ddt
class LoginTestCase(unittest.TestCase):
    sheet_name = 'login'
    my_generate.generate(sheet_name, file_path, yaml_file)
    wb = ReadExcel(file_path, sheet_name)
    cases = wb.read_data_obj()

    @classmethod
    def tearDownClass(cls):
        # login
        cls.wb.w_save()
        cls.wb.wb.close()

    @data(*cases)
    def test(self, case):
        my_log.info(f'TestCase {case.case_name} starting------')

        actual = testRequest.request(method=case.method, url=case.url, data=eval(case.request_data),
                                     params=eval(case.request_data))
        actual = json.loads(actual)
        expect = json.loads(case.expected_data)
        try:
            result = None
            self.assertEqual((expect['status'], expect['code']), (actual['status'], actual['code']))
        except AssertionError as e:
            print('Not Passed...')
            result = 'failed'
            print(f"{expect['msg']}\n{actual['msg']}")
            my_log.error(f'【Failed】：E{expect} != A{actual}')
            raise e
        else:
            print('Passed')
            result = 'passed'
            my_log.info(f'【Success】：E{expect} == A{actual}')
        finally:
            self.wb.w_data(case.row, self.wb.r_max()[1], result)
            my_log.info(f'TestCase {case.case_name} end------')
            # self.wb.w_save()


@ddt
class RegisterTestCase(unittest.TestCase):
    sheet_name = 'register'
    my_generate.generate(sheet_name, file_path, yaml_file)
    wb = ReadExcel(file_path, sheet_name)
    cases = wb.read_data_obj()

    @classmethod
    def tearDownClass(cls):
        cls.wb.w_save()
        cls.wb.wb.close()

    @data(*cases)
    def test(self, case):
        my_log.info(f'TestCase {case.case_name} starting------')

        actual = testRequest.request(method=case.method, url=case.url, data=eval(case.request_data),
                                     params=eval(case.request_data))
        actual = json.loads(actual)
        expect = json.loads(case.expected_data)
        try:
            result = None
            self.assertEqual((expect['status'], expect['code']), (actual['status'], actual['code']))
        except AssertionError as e:
            print('Not Passed...')
            result = 'failed'
            print(f"{expect['msg']}\n{actual['msg']}")
            my_log.error(f'【Failed】：E{expect} != A{actual}')
            raise e
        else:
            print('Passed')
            result = 'passed'
            my_log.info(f'【Success】：E{expect} == A{actual}')
        finally:
            # 2
            self.wb.w_data(case.row, self.wb.r_max()[1], result)
            my_log.info(f'TestCase {case.case_name} end------')
            # self.wb.w_save()


@ddt
class RechargeTestCase(unittest.TestCase):
    sheet_name = 'recharge'
    my_generate.generate(sheet_name, file_path, yaml_file)
    wb = ReadExcel(file_path, sheet_name)
    cases = wb.read_data_obj()

    @classmethod
    def setUpClass(cls):
        testRequest.request(method='post', url='http://test.lemonban.com/futureloan/mvc/api/member/login',
                            data={"mobilephone": "13912345611", "pwd": "123456"})

    @classmethod
    def tearDownClass(cls):
        cls.wb.w_save()
        cls.wb.wb.close()

    @data(*cases)
    def test(self, case):
        my_log.info(f'TestCase {case.case_name} starting------')
        expect = json.loads(case.expected_data)
        sql = f'SELECT leaveamount FROM member where mobilephone = {case.mobilephone}'

        amount = case.amount if expect['code'] == '10001' else 0
        flag = False if case.mobilephone is None or case.amount is None else True
        try:
            if flag:
                con1 = Mysql()
                amount_bf = con1.select(sql)[0] if con1.select(sql) is not None else 0
            actual = testRequest.request(method=case.method, url=case.url, data=eval(case.request_data),
                                         params=eval(case.request_data))
            actual = json.loads(actual)
            if flag:
                con2 = Mysql()
                amount_af = con2.select(sql)[0] if con2.select(sql) is not None else 0
            self.assertEqual((expect['status'], expect['code']), (actual['status'], actual['code']))
            self.assertEqual(amount, amount_af - amount_bf) if flag else print('未校验金额')
        except (AssertionError, TypeError) as e:
            print(f"Not Passed...\n{expect['msg']}\n{actual['msg']}")
            result = 'failed'
            my_log.error(f'【Failed】：E{expect} != A{actual}')
            raise e
        else:
            print('Passed')
            result = 'passed'
            my_log.info(f'【Success】：E{expect} == A{actual}')
        finally:
            # 2
            self.wb.w_data(case.row, self.wb.r_max()[1], result)
            my_log.info(f'TestCase {case.case_name} end------')
            # self.wb.w_save()


@ddt
class WithDrawTestCase(unittest.TestCase):
    sheet_name = 'withdraw'
    my_generate.generate(sheet_name, file_path, yaml_file)
    wb = ReadExcel(file_path, sheet_name)
    cases = wb.read_data_obj()

    @classmethod
    def setUpClass(cls):
        testRequest.request(method='post', url='http://test.lemonban.com/futureloan/mvc/api/member/login',
                            data={"mobilephone": "13912345611", "pwd": "123456"})

    @classmethod
    def tearDownClass(cls):
        cls.wb.w_save()
        cls.wb.wb.close()

    @data(*cases)
    def test(self, case):
        my_log.info(f'TestCase {case.case_name} starting------')
        expect = json.loads(case.expected_data)
        sql = f'SELECT leaveamount FROM member where mobilephone = {case.mobilephone}'

        amount = case.amount if expect['code'] == '10001' else 0
        flag = False if case.mobilephone is None or case.amount is None else True
        try:
            if flag:
                con1 = Mysql()
                amount_bf = con1.select(sql)[0] if con1.select(sql) is not None else 0
            actual = testRequest.request(method=case.method, url=case.url, data=eval(case.request_data),
                                         params=eval(case.request_data))
            actual = json.loads(actual)
            if flag:
                con1.commit()
                # con2 = Mysql()
                amount_af = con1.select(sql)[0] if con1.select(sql) is not None else 0
                self.assertEqual(amount, amount_bf - amount_af) if flag else print('未校验金额')
            self.assertEqual((expect['status'], expect['code']), (actual['status'], actual['code']))
        except (AssertionError, TypeError) as e:
            print(f"Not Passed...\n{expect['msg']}\n{actual['msg']}")
            result = 'failed'
            my_log.error(f'【Failed】：E{expect} != A{actual}')
            raise e
        else:
            print('Passed')
            result = 'passed'
            my_log.info(f'【Success】：E{expect} == A{actual}')
        finally:
            # 2
            self.wb.w_data(case.row, self.wb.r_max()[1], result)
            my_log.info(f'TestCase {case.case_name} end------')
            # self.wb.w_save()


if __name__ == '__main__':
    unittest.main()
