# @File   :   R_r_config.py.py
# @Author :   July401
# @Date   :   2019/6/3
# @Email  :   july401@qq.com

import configparser
from package_102.common.R_r_os import my_os

config_path = my_os.readpath('config') + 'config.ini'


class Config_data(configparser.ConfigParser):
    def __init__(self):
        super().__init__()
        self.read(config_path)


my_config = Config_data()

