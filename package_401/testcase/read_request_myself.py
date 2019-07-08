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

api = my_config.get('env', 'api')

file_name = my_config.get('excel', 'file_name')
file_path = f'{DATA_DIR}{file_name}'
yaml_file = f'{CONF_DIR}parms.yaml'


def get_ret(request_url, request_data, method_name):
    try:
        web_service = client.Client(url=request_url)
        if method_name == 'sendMCode':
            actual = web_service.service.sendMCode(eval(request_data))
        elif method_name == 'sendSM':
            actual = web_service.service.sendMCode(eval(request_data))
        elif method_name == 'sendSM':
            actual = web_service.service.sendMCode(eval(request_data))
    except WebFault as e:
        actual = {'retCode': e.fault.faultcode, 'retInfo': e.fault.faultstring}
        print(e)
    else:
        actual = dict(actual)
    return actual


def do_assert(actual, expect, cls, case):
    try:
        cls.assertEqual(expect["retCode"], actual['retCode'])
    except AssertionError as e:
        print('Not Passed...')
        result = 'failed'
        print(case.request_data)
        my_log.error(f'【Failed】：E{expect} != A{actual}')
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
        if case.checksql:
            mobile = eval(case.request_data)['mobile']
            setattr(ParmTemp, 'mobile', mobile)
            setattr(ParmTemp, 'tableno', mobile[-3:-2])
            setattr(ParmTemp, 'dbno', mobile[-2:])
            case.checksql = my_replace(case.checksql)
            db2check = Mysql(f"sms_db_{ParmTemp.dbno}")
            verify_code = db2check.select(case.checksql)
            self.assertNotEqual(verify_code, None)


@ddt
class TestUserRegister(unittest.TestCase):
    sheet_name = 'userRegister'
    wb = ReadExcel(file_path, sheet_name)
    cases = wb.read_data_obj()

    @classmethod
    def tearDownClass(cls):
        pass

    @data(*cases)
    def test(self, case):
        my_log.info(f'TestCase {case.case_name} starting------')
        case.url = api + case.url
        case.request_data = my_replace(case.request_data)
        actual = get_ret(case.url, case.request_data, 'userRegister')
        expect = json.loads(case.expected_data)
        do_assert(actual, expect, self, case)
        if case.api_name == 'sendMCode':
            mobile = eval(case.request_data)['mobile']
            setattr(ParmTemp, 'mobile', mobile)
            setattr(ParmTemp, 'tableno', mobile[-3:-2])
            setattr(ParmTemp, 'dbno', mobile[-2:])
            case.checksql = my_replace(case.checksql)
            db2check = Mysql(f"sms_db_{ParmTemp.dbno}")
            verify_code = db2check.select(case.checksql)[0]
            setattr(ParmTemp, 'verify_code', verify_code)
        if case.checksql:
            mobile = eval(case.request_data)['mobile']
            setattr(ParmTemp, 'mobile', mobile)
            setattr(ParmTemp, 'tableno', mobile[-3:-2])
            setattr(ParmTemp, 'dbno', mobile[-2:])
            case.checksql = my_replace(case.checksql)
            db2check = Mysql(f"sms_db_{ParmTemp.dbno}")
            verify_code = db2check.select(case.checksql)
            self.assertNotEqual(verify_code, None)
