import json
import unittest

from package_201.common.R_r_config import my_config
from package_201.common.R_r_excel import ReadExcel
from package_201.common.R_r_log import my_log
from package_201.common.R_r_os import DATA_DIR, CONF_DIR
from package_201.common.R_request import HttpRequestNoCookie, HttpRequest
from package_201.common.generate import Generate
from package_201.library.ddt import ddt, data

file_name = my_config.get('excel', 'file_name')
file_path = f'{DATA_DIR}{file_name}'
sheet_name = 'add'
columns_read = my_config.get('excel', 'columns_read')

testRequestNoCookie = HttpRequestNoCookie()
testRequest = HttpRequest()

my_generate = Generate(file_path, sheet_name, yaml_file=f'{CONF_DIR}parms.yaml')
my_generate.generate()

wb = ReadExcel(file_path, sheet_name)
# cases = wb.r_data_obj_from_column(eval(columns_read))
cases = wb.read_data_obj()


@ddt
class AddTestCase(unittest.TestCase):

    def setUp(self) -> None:
        print('\n' + 'start'.center(32, '-'))

    def tearDown(self) -> None:
        print('end'.center(32, '-'))

    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        wb.w_save()

    @data(*cases)
    def testAdd(self, case):
        my_log.info(f'TestCase {case.case_name} starting------')
        # login session
        testRequest.request(method='post', url='http://test.lemonban.com/futureloan/mvc/api/member/login',
                            data={"mobilephone": "13912345611", "pwd": "123456"})
        actual = testRequest.request(method=case.method, url=case.url, data=eval(case.request_data),
                                     params=eval(case.request_data))
        # actual = register(*eval(case.data))
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
            my_log.info(f'【Success】')
        finally:
            wb.w_data(case.row + 1, wb.r_max()[1], result)
            my_log.info(f'TestCase {case.case_name} end------')


if __name__ == '__main__':
    unittest.main()
