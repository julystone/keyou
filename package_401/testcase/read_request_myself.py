import json
import unittest

from suds import client, WebFault

from package_401.common.R_r_config import my_config
from package_401.common.R_r_excel import ReadExcel
from package_401.common.R_r_log import my_log
from package_401.common.R_r_os import DATA_DIR, CONF_DIR
from package_401.library.ddt import ddt, data
from package_401.common.R_r_sql import Mysql
from package_401.common.R_r_re import myRex, ParmTemp
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


class CommonMethods:
    @staticmethod
    def get_ret(case):
        try:
            web_service = client.Client(url=case.url)
            string = f'web_service.service.{case.api_name}({case.request_data})'
            actual = eval(string)
        except WebFault as e:
            actual = {'retCode': e.fault.faultcode, 'retInfo': e.fault.faultstring}
            print(e)
        else:
            actual = dict(actual)
        return actual

    def do_sql(self, sql):
        print(self.db.affect(sql))
        return self.db.select(sql)[0]

@ddt
class TestSendMCode(unittest.TestCase, CommonMethods):
    sheet_name = 'sendMCode'
    wb = ReadExcel(file_path, sheet_name)
    cases = wb.read_data_obj()

    @classmethod
    def setUpClass(cls) -> None:
        cls.db = Mysql()

    @data(*cases)
    def test(self, case):
        my_log.info(f'TestCase {case.case_name} starting------')
        case.url = api + case.url
        actual = self.get_ret(case)
        expect = json.loads(case.expected_data)
        do_assert(actual, expect, self, case)
        if case.checkSql:
            mobile = eval(case.request_data)['mobile']
            setattr(ParmTemp, 'mobile', mobile)
            setattr(ParmTemp, 'tableno', mobile[-3:-2])
            setattr(ParmTemp, 'dbno', mobile[-2:])
            case.checkSql = myRex.my_replace(case.checkSql)
            verify_code = self.db.affect(case.checkSql)
            self.assertNotEqual(verify_code, None)


@ddt
class TestUserRegister(unittest.TestCase, CommonMethods):
    sheet_name = 'userRegister'
    wb = ReadExcel(file_path, sheet_name)
    cases = wb.read_data_obj()

    @classmethod
    def setUpClass(cls) -> None:
        setattr(ParmTemp, 'randomNo', one_number(6))
        setattr(ParmTemp, 'unRegPhone', one_number(11))
        cls.db = Mysql()

    @data(*cases)
    def test(self, case):
        my_log.info(f'TestCase {case.case_name} starting------')
        # 数据预处理
        case.url = api + case.url
        # ParmTemp.__setattr__('randomNo', one_number(6))
        if case.preSql:
            case.preSql = myRex.my_replace(case.preSql)
            res = self.do_sql(case.preSql)
            attr = myRex.my_find(case.preSql, "as (.*?) from")
            setattr(ParmTemp, attr, res)
        case.request_data = myRex.my_replace(case.request_data)
        actual = self.get_ret(case)
        expect = json.loads(case.expected_data)
        do_assert(actual, expect, self, case)
        if case.checkSql:
            mobile = eval(case.request_data)['mobile']
            setattr(ParmTemp, 'mobile', mobile)
            setattr(ParmTemp, 'tableno', mobile[-3:-2])
            setattr(ParmTemp, 'dbno', mobile[-2:])
            case.checkSql = myRex.my_replace(case.checkSql)
            verify_code = self.do_sql(case.checkSql)
            self.assertNotEqual(verify_code, None)
