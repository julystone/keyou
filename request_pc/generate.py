# @File   :   generate.py
# @Author :   July401
# @Date   :   2019/6/11
# @Email  :   july401@qq.com

import json

import yaml

from request_pc import R_r_excel

file_name = "./api_test.xlsx"
sheet_name = 'Sheet1'
yaml_file = './parms.yaml'


def yaml_read(yamlfile):
    with open(yamlfile) as f:
        conf = yaml.safe_load(f)
        title = list(conf)
        return conf, title


def sample_data_json(item, list2convert):
    if list2convert is None:
        return {}
    values = []
    key_all = list2convert.keys()
    for key in key_all:
        if list2convert[key] == 'str':
            # 若为str，给excel的数据加上"". 当前仅仅对str特殊化处理，后续可增加
            values.append(f"{getattr(item, key)}")
        else:
            values.append(getattr(item, key))
    result = dict(zip(key_all, values))
    return result


def write_in(item, conf, title, Noneflag=1):
    for x in range(len(title)):
        name = list(title[x])[0]
        if item.api_name == name:
            break
    api_list = conf[x][name]

    res1 = sample_data_json(item, api_list)
    res2 = sample_data_json(item, {"status": "int", "code": "str", "data": "object", "msg": "str"})
    list2del = []
    for key in res1.keys():
        if res1[key] == 'None' or res1[key] is None:
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
    expected_data = json.dumps(res2, ensure_ascii=False)
    # request_data = str(res1)
    # expected_data = str(res2) # 直接强转换为str，双引号会变成单引号，暂不知如何解决
    origin_data.w_data(item.case_id + 1, 7, request_data)
    origin_data.w_data(item.case_id + 1, 8, expected_data)


if __name__ == '__main__':
    origin_data = R_r_excel.ReadExcel(file_name, sheet_name)
    rows = origin_data.read_data_obj()
    (conf, title) = yaml_read(yaml_file)
    progress = 1
    for item in rows:
        print(progress, end='->')
        write_in(item, conf, title, Noneflag=1)
        progress += 1
    origin_data.w_save()  # 此处需要修改完毕后，单独保存，否则性能很差
    print('>end<'.center(64, '-'))
