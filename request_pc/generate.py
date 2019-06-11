# @File   :   Pds_Pc.py
# @Author :   July401
# @Date   :   2019/5/30
# @Email  :   july401@qq.com

import datetime
import json
from request_pc import R_r_excel

file_name = "api_test.xlsx"
sheet_name = 'Sheet_all'

origin_data = R_r_excel.ReadExcel(file_name, sheet_name)


def sample_data_json(item, list2convert):
    key_all = []
    for i in list2convert:
        key_all.append(i['name'])
    values = []
    for x in range(len(key_all)):
        if list2convert[x]['type'] == 'str':
            values.append(f"{getattr(item, key_all[x])}") # 若为str，给excel输入数据，加上""
        # elif list2convert[x]['type'] == 'int': # 当前仅仅对str特殊化处理，后续可增加
        else:
            values.append(getattr(item, key_all[x]))
    result = dict(zip(key_all, values))
    return result


def write_in(item, Noneflag=1):
    # 此处
    if item.api_name == 'register':
        api_list = [{"name": "mobilephone", "type": "str"}, {"name": "pwd", "type": "str"},
                    {"name": "regname", "type": "str"}]
    elif item.api_name == 'login':
        api_list = [{"name": "mobilephone", "type": "str"}, {"name": "pwd", "type": "str"}]
    elif item.api_name == 'recharge':
        api_list = [{"name": "mobilephone", "type": "str"}, {"name": "amount", "type": "double"}]
    elif item.api_name == 'withdraw':
        api_list = [{"name": "mobilephone", "type": "str"}, {"name": "amount", "type": "double"}]
    elif item.api_name == 'list':
        api_list = []
    elif item.api_name == 'bidLoan':
        api_list = [{"name": "memberId", "type": "int"}, {"name": "password", "type": "str"},
                    {"name": "loanId", "type": "double"}, {"name": "amount", "type": "double"}]
    elif item.api_name == 'add':
        api_list = [{"name": "memberId", "type": "int"}, {"name": "title", "type": "str"},
                    {"name": "amount", "type": "double"}, {"name": "loanRate", "type": "double"},
                    {"name": "loanTerm", "type": "int"}, {"name": "loanDateType", "type": "int"},
                    {"name": "repaymemtWay", "type": "int"}, {"name": "biddingDays", "type": "int"}]
    else:
        return
    res1 = sample_data_json(item, api_list)
    res2 = sample_data_json(item, [{"name": "status", "type": "int"}, {"name": "code", "type": "str"},
                                   {"name": "data", "type": "object"}, {"name": "msg", "type": "str"}])
    list2del = []
    for key, value in res1.items():
        if value == 'None' or value == None:
            list2del.append(key)
    if Noneflag == 1:
        # 方案1：将None的参数去除掉
        for x in list2del:
            res1.pop(x)
    elif Noneflag == 2:
        # 方案2：将None的参数统一赋值成None   但是现在有问题，被json.dumps后，会变成null。暂不知如何解决
        for x in list2del:
            res1[x] = None

    request_data = json.dumps(res1, ensure_ascii=False)
    # request_data = str(res1)
    expected_data = json.dumps(res2, ensure_ascii=False)
    # expected_data = str(res2) # 直接强转换为str，双引号会变成单引号，暂不知如何解决
    time_start = datetime.datetime.now()
    origin_data.w_data(item.case_id + 1, 7, request_data)
    origin_data.w_data(item.case_id + 1, 8, expected_data)
    time_end = datetime.datetime.now()
    print(f'{time_end - time_start}')


list1 = origin_data.read_data_obj()
progress = 1
for item in list1:
    print(progress, end='->')
    write_in(item, Noneflag=1)
    progress += 1
origin_data.w_save() # 此处需要修改完毕后，单独保存，否则性能很差
print('>end<'.center(64, '-'))
