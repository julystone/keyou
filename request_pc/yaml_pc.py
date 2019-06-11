# @File   :   yaml_pc.py
# @Author :   July401
# @Date   :   2019/6/11
# @Email  :   july401@qq.com


import yaml

with open("./config.yaml") as f:
    res = yaml.safe_load(f)
    for i in res:
        # print(list(i))
        print(i)