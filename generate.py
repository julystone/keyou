# @File   :   Pds_Pc.py
# @Author :   July401
# @Date   :   2019/5/30
# @Email  :   july401@qq.com

import openpyxl
from package_102.common import R_r_excel
import json

file_name = "api_test.xlsx"
sheet_name = 'Sheet1'
# 打开工作簿
wb = openpyxl.load_workbook(file_name)
# 选择表单
sheet = wb[sheet_name]

origin_data = R_r_excel.ReadExcel(file_name, sheet_name)


def register(item):
    request_data = f"""{{"mobilephone":"{item.mobilephone}", "pwd":"{item.pwd}", "nickname":"{item.regname}"}}"""
    json.dump(request_data)
    print(json)
    expected_data = f"""{{"status":"{item.status}", "code":"{item.code}", "data":"{item.data}", "msg":"{item.msg}"}}"""
    json.dump(request_data)
    print(json)
    origin_data.w_data(item.case_id + 1, 7, request_data)
    origin_data.w_data(item.case_id + 1, 8, expected_data)


def login(item):
    request_data = f"""{{"mobilephone":"{item.mobilephone}", "pwd":"{item.pwd}"}}"""
    expected_data = f"""{{"status":"{item.status}", "code":"{item.code}", "data":"{item.data}", "msg":"{item.msg}"}}"""
    origin_data.w_data(item.case_id + 1, 7, request_data)
    origin_data.w_data(item.case_id + 1, 8, expected_data)


def recharge(item):
    request_data = f"""{{"mobilephone":"{item.mobilephone}", "amount":"{item.amount}"}}"""
    expected_data = f"""{{"status":"{item.status}", "code":"{item.code}", "data":"{item.data}", "msg":"{item.msg}"}}"""
    origin_data.w_data(item.case_id + 1, 7, request_data)
    origin_data.w_data(item.case_id + 1, 8, expected_data)


def withdraw(item):
    request_data = f"""{{"mobilephone":"{item.mobilephone}", "amount":"{item.amount}"}}"""
    expected_data = f"""{{"status":"{item.status}", "code":"{item.code}", "data":"{item.data}", "msg":"{item.msg}"}}"""
    origin_data.w_data(item.case_id + 1, 7, request_data)
    origin_data.w_data(item.case_id + 1, 8, expected_data)


list1 = origin_data.read_data_obj()

for item in list1:
    if item.api_name == 'register':
        register(item)
    # elif item.api_name == 'login':
    #     login(item)
    # elif item.api_name == 'recharge':
    #     recharge(item)
    # elif item.api_name == 'withdraw':
    #     withdraw(item)
