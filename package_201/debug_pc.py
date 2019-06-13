# @File   :   debug_pc.py
# @Author :   July401
# @Date   :   2019/6/3
# @Email  :   july401@qq.com

import os
import shutil

from package_201.common.R_r_os import DATA_DIR

# cf = configparser.ConfigParser()
# cf.read('july_config.cfg', encoding='utf8')
# print(cf.sections())
# print(cf.options('log_settings'))
# cc = cf.get('log_settings', 'log_path')
# dd = __file__
# print(type(cc))
# print(type(dd))
# print(cc)
# print(dd)
# shutil.copy(file_path, file_path + '.bak')
shutil.copytree(DATA_DIR, os.path.join(DATA_DIR, 'bak'))
