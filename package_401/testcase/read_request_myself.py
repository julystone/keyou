import json
import unittest

from suds import client, WebFault

from package_401.common.R_r_config import my_config
from package_401.common.R_r_excel import ReadExcel
from package_401.common.R_r_log import my_log
from package_401.common.R_r_os import DATA_DIR, CONF_DIR
from package_401.library.ddt import ddt, data
from package_401.common.R_r_sql import Mysql
from package_401.common.R_r_re import my_replace, ParmTemp
import random

api = my_config.get('env', 'api')

file_name = my_config.get('excel', 'file_name')
file_path = f'{DATA_DIR}{file_name}'
yaml_file = f'{CONF_DIR}parms.yaml'


def one_number(number):
    head = '139'
    for _ in range(number - len(head)):
        head += str(random.randint(0, 9))
    return head


def get_ret(request_url, request_data, method_name):
    try:
        web_service = client.Client(url=request_url)
        string = f'web_service.service.{method_name}({request_data})'
        actual = eval(string)
    except WebFault as e:
        actual = {'retCode': e.fault.faultcode, 'retInfo': e.fault.faultstring}
        print(e)
    else:
        actual = dict(actual)
    return actual


def do_assert(actual, expect, cls, case):
    try:
        cls.assertEqual((expect["retCode"], expect['retInfo']), (actual['retCode'], actual['retInfo']))
    except AssertionError as e:
        print('Not Passed...')
        result = 'failed'
        print(case.request_data)
        my_log.error(f'【Failed】：E{expect} != A{actual}')
        print(f'E{expect}\nA{actual}')
        raise e
    else:
        print('Passed')
        result = 'passed'
        my_log.info(f'【Success】：E{expect} == A{actual}')
    finally:
        cls.wb.w_data(case.row, cls.wb.r_max()[1], result)
        my_log.info(f'TestCase {case.case_name} end------')
    return result


@ddt
class TestSendMCode(unittest.TestCase):
    sheet_name = 'sendMCode'
    wb = ReadExcel(file_path, sheet_name)
    cases = wb.read_data_obj()

    @classmethod
    def tearDownClass(cls):
        pass

    @data(*cases)
    def test(self, case):
        my_log.info(f'TestCase {case.case_name} starting------')
        case.url = api + case.url
        actual = get_ret(case.url, case.request_data, 'sendMCode')
        expect = json.loads(case.expected_data)
        do_assert(actual, expect, self, case)
        if case.checkSql:
            mobile = eval(case.request_data)['mobile']
            setattr(ParmTemp, 'mobile', mobile)
            setattr(ParmTemp, 'tableno', mobile[-3:-2])
            setattr(ParmTemp, 'dbno', mobile[-2:])
            case.checkSql = my_replace(case.checkSql)
            db2check = Mysql(f"sms_db_{ParmTemp.dbno}")
            verify_code = db2check.select(case.checkSql)
            self.assertNotEqual(verify_code, None)


@ddt
class TestUserRegister(unittest.TestCase):
    sheet_name = 'userRegister'
    wb = ReadExcel(file_path, sheet_name)
    cases = wb.read_data_obj()

    @data(*cases)
    def test(self, case):
        my_log.info(f'TestCase {case.case_name} starting------')
        # 数据预处理
        case.url = api + case.url
        if case.preSql:
            case.preSql = my_replace(case.preSql)
            db2pre = Mysql('user_db')
            res = db2pre.select(case.preSql)[0]
            setattr(ParmTemp, 'uid', res)
        case.request_data = my_replace(case.request_data)
        actual = get_ret(case.url, case.request_data, case.api_name)
        expect = json.loads(case.expected_data)
        do_assert(actual, expect, self, case)
        if case.checkSql:
            mobile = eval(case.request_data)['mobile']
            setattr(ParmTemp, 'mobile', mobile)
            setattr(ParmTemp, 'tableno', mobile[-3:-2])
            setattr(ParmTemp, 'dbno', mobile[-2:])
            case.checkSql = my_replace(case.checkSql)
            db2check = Mysql(f"sms_db_{ParmTemp.dbno}")
            verify_code = db2check.select(case.checkSql)[0]
            self.assertNotEqual(verify_code, None)
            setattr(ParmTemp, 'verify_code', verify_code)