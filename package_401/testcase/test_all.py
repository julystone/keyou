import json
import random
import unittest

from package_401.common.R_r_config import my_config
from package_401.common.R_r_excel import ReadExcel
from package_401.common.R_r_log import my_log
from package_401.common.R_r_os import DATA_DIR, CONF_DIR
from package_401.common.R_r_re import my_replace, ParmTemp
from package_401.common.R_r_sql import Mysql
from package_401.common.R_r_sql import my_sql
from package_401.common.R_request import HttpRequestNoCookie, HttpRequest
from package_401.library.ddt import ddt, data

api = my_config.get('env', 'api')
file_name = my_config.get('excel', 'file_name')
file_path = f'{DATA_DIR}{file_name}'
yaml_file = f'{CONF_DIR}parms.yaml'
# sheet_name = 'login'

testRequestNoCookie = HttpRequestNoCookie()
testRequest = HttpRequest()


def one_number(number):
    head = '139'
    for _ in range(number - len(head)):
        head += str(random.randint(0, 9))
    return head


@ddt
class LoginTestCase(unittest.TestCase):
    sheet_name = 'login'
    wb = ReadExcel(file_path, sheet_name)
    cases = wb.read_data_obj()

    @classmethod
    def tearDownClass(cls):
        pass

    @data(*cases)
    def test(self, case):
        my_log.info(f'TestCase {case.case_name} starting------')
        case.url = api + case.url
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


@ddt
class RegisterTestCase(unittest.TestCase):
    sheet_name = 'register'
    wb = ReadExcel(file_path, sheet_name)
    con = Mysql()
    cases = wb.read_data_obj()

    @classmethod
    def tearDownClass(cls):
        pass

    def checkNumber(self, case):
        number = None
        while '#reg_phone#' in case.request_data:
            number = one_number(11)
            sql = f"select * from member where mobilephone = {number}"
            if self.con.select(sql) is None:
                break
        return number

    @data(*cases)
    def test(self, case):
        my_log.info(f'TestCase {case.case_name} starting------')
        number = self.checkNumber(case)
        case.request_data = my_replace(case.request_data, content=number)
        case.url = api + case.url
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


@ddt
class RechargeTestCase(unittest.TestCase):
    sheet_name = 'recharge'
    wb = ReadExcel(file_path, sheet_name)
    cases = wb.read_data_obj()

    @classmethod
    def setUpClass(cls):
        testRequest.request(method='post', url='http://test.lemonban.com/futureloan/mvc/api/member/login',
                            data={"mobilephone": "13912345611", "pwd": "123456"})

    @classmethod
    def tearDownClass(cls):
        cls.wb.save()

    @data(*cases)
    def test(self, case):
        my_log.info(f'TestCase {case.case_name} starting------')
        case.request_data = my_replace(case.request_data)
        case.url = api + case.url

        expect = json.loads(case.expected_data)

        amount = case.amount if case.checksql else 0
        if case.checksql:
            case.checksql = my_replace(case.checksql)
            amount_bf = my_sql.select(case.checksql)[0]
        actual = testRequest.request(method=case.method, url=case.url, data=eval(case.request_data),
                                     params=eval(case.request_data))
        actual = json.loads(actual)
        if case.checksql:
            amount_af = my_sql.select(case.checksql)[0]
        try:
            self.assertEqual((expect['status'], expect['code']), (actual['status'], actual['code']))
            self.assertEqual(amount, amount_af - amount_bf) if case.checksql else print('未校验金额')
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
            # self.wb.save()


@ddt
class WithDrawTestCase(unittest.TestCase):
    sheet_name = 'withdraw'
    wb = ReadExcel(file_path, sheet_name)
    cases = wb.read_data_obj()

    @classmethod
    def setUpClass(cls):
        testRequest.request(method='post', url='http://test.lemonban.com/futureloan/mvc/api/member/login',
                            data={"mobilephone": "13912345611", "pwd": "123456"})

    @classmethod
    def tearDownClass(cls):
        pass

    @data(*cases)
    def test(self, case):
        my_log.info(f'TestCase {case.case_name} starting------')
        case.request_data = my_replace(case.request_data)
        case.url = api + case.url

        expect = json.loads(case.expected_data)

        amount = case.amount if case.checksql else 0
        if case.checksql:
            case.checksql = my_replace(case.checksql)
            amount_bf = my_sql.select(case.checksql)[0]
        actual = testRequest.request(method=case.method, url=case.url, data=eval(case.request_data),
                                     params=eval(case.request_data))
        actual = json.loads(actual)
        if case.checksql:
            amount_af = my_sql.select(case.checksql)[0]
        result = None
        try:
            self.assertEqual((expect['status'], expect['code']), (actual['status'], actual['code']))
            self.assertEqual(amount, amount_bf - amount_af) if case.checksql else print('未校验金额')
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


@ddt
class AddTestCase(unittest.TestCase):
    sheet_name = 'add'
    wb = ReadExcel(file_path, sheet_name)
    cases = wb.read_data_obj()

    @classmethod
    def setUpClass(cls):
        testRequest.request(method='post', url='http://test.lemonban.com/futureloan/mvc/api/member/login',
                            data={"mobilephone": "13912345611", "pwd": "123456"})

    @classmethod
    def tearDownClass(cls):
        pass

    @data(*cases)
    def test(self, case):
        my_log.info(f'TestCase {case.case_name} starting------')
        case.request_data = my_replace(case.request_data)
        case.url = api + case.url

        expect = json.loads(case.expected_data)
        if case.checksql:
            case.checksql = my_replace(case.checksql)
            id_old = my_sql.select(case.checksql)[0] if my_sql.select(case.checksql) is not None else None
        actual = testRequest.request(method=case.method, url=case.url, data=eval(case.request_data),
                                     params=eval(case.request_data), timeout=5)
        actual = json.loads(actual) if actual is not None else None
        if case.checksql:
            id_new = my_sql.select(case.checksql)[0]
        result = None
        try:
            self.assertEqual((expect['status'], expect['code']), (actual['status'], actual['code']))
            self.assertNotEqual(id_old, id_new) if case.checksql else True
        except (AssertionError, TypeError) as e:
            print(f"Not Passed...\n{expect['msg']}\n{actual['msg']}")
            print(f"\n请求参数为{case.request_data}")
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


@ddt
class AuditTestCase(unittest.TestCase):
    sheet_name = 'audit'
    wb = ReadExcel(file_path, sheet_name)
    cases = wb.read_data_obj()

    @classmethod
    def setUpClass(cls):
        testRequest.request(method='post', url='http://test.lemonban.com/futureloan/mvc/api/member/login',
                            data={"mobilephone": "13912345611", "pwd": "123456"})
        cls.loan = my_sql.select("SELECT id FROM loan WHERE MemberID = 85010 and `Status` = 1")[0]
        setattr(ParmTemp, 'loanId', str(cls.loan))

    @classmethod
    def tearDownClass(cls):
        pass

    @data(*cases)
    def test(self, case):
        my_log.info(f'TestCase {case.case_name} starting------')
        case.request_data = my_replace(case.request_data)
        case.url = api + case.url

        expect = json.loads(case.expected_data)
        if case.checksql:
            case.checksql = my_replace(case.checksql)
            status_old = my_sql.select(case.checksql)[0] if my_sql.select(case.checksql) is not None else None
        actual = testRequest.request(method=case.method, url=case.url, data=eval(case.request_data),
                                     params=eval(case.request_data), timeout=5)
        actual = json.loads(actual) if actual is not None else None
        if case.checksql:
            status_new = my_sql.select(case.checksql)[0]
        result = None
        try:
            self.assertEqual((expect['status'], expect['code']), (actual['status'], actual['code']))
            self.assertEqual(status_new - status_old, 1) if case.checksql else True
        except (AssertionError, TypeError) as e:
            print(f"Not Passed...\n{expect['msg']}\n{actual['msg']}")
            print(f"\n请求参数为{case.request_data}")
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


if __name__ == '__main__':
    unittest.main()
