# @File   :   Pds_Pc.py
# @Author :   July401
# @Date   :   2019/5/30
# @Email  :   july401@qq.com

import json

import openpyxl

from package_102.common import R_r_excel

file_name = "api_test.xlsx"
sheet_name = 'Sheet2'
# 打开工作簿
wb = openpyxl.load_workbook(file_name)
# 选择表单
sheet = wb[sheet_name]

origin_data = R_r_excel.ReadExcel(file_name, sheet_name)


def sample_data_json(item, list2convert):
    keys = list2convert
    values = []
    for x in keys:
        values.append(f"{getattr(item, x)}")
    result = dict(zip(keys, values))
    return result


def write_in(item):
    if item.api_name == 'register':
        res1 = sample_data_json(item, ["mobilephone", "pwd", "regname"])
    elif item.api_name == 'login':
        res1 = sample_data_json(item, ["mobilephone", "pwd"])
    elif item.api_name == 'recharge':
        res1 = sample_data_json(item, ["mobilephone", "amount"])
    elif item.api_name == 'withdraw':
        res1 = sample_data_json(item, ["mobilephone", "amount"])
    elif item.api_name == 'list':
        res1 = sample_data_json(item, [])
    elif item.api_name == 'bidLoan':
        res1 = sample_data_json(item, ["memberId", "password", "loanId", "amount"])
    elif item.api_name == 'add':
        res1 = sample_data_json(item, ["memberId", "title", "amount", "loanRate", "loanTerm", "loanDateType", "repaymemtWay", "biddingDays"])
    else:
        return
    res2 = sample_data_json(item, ["status", "code", "data", "msg"])
    list2del = []
    for key, value in res1.items():
        if value == 'None' or key == 'None':
            list2del.append(key)
    for x in list2del:
        res1.pop(x)
    request_data = json.dumps(res1, ensure_ascii=False)
    expected_data = json.dumps(res2, ensure_ascii=False)
    origin_data.w_data(item.case_id + 1, 7, request_data)
    origin_data.w_data(item.case_id + 1, 8, expected_data)


list1 = origin_data.read_data_obj()
progress = 0
for item in list1:
    write_in(item)
    progress += 1
    print(progress, end='->')
print('end'.center('-', 128))
