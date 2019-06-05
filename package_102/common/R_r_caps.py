# @File   :   R_r_caps.py
# @Author :   July401
# @Date   :   2019/6/5
# @Email  :   july401@qq.com

import yaml
from package_102.common.R_r_os import my_os


class CapsRead:
    def read_caps(self):
        yaml_path = my_os.readpath('config') + r'caps.yaml'
        with open(yaml_path, 'r', encoding='utf-8') as f:
            data = yaml.load(f)
            return data


my_caps = CapsRead()
