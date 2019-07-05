# @File   :   R_r_config.py.py
# @Author :   July401
# @Date   :   2019/6/3
# @Email  :   july401@qq.com

import configparser

from package_301.common.R_r_os import CONF_DIR

config_path = CONF_DIR


class ConfigData(configparser.ConfigParser):
    def __init__(self, choice=0):
        super().__init__()
        if choice == 0:
            self.read(config_path + 'config.ini')
        else:
            self.read(config_path + 'config1.ini')


my_config = ConfigData()
