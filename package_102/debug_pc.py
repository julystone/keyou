# @File   :   debug_pc.py
# @Author :   July401
# @Date   :   2019/6/3
# @Email  :   july401@qq.com

import configparser


cf = configparser.ConfigParser()
cf.read('july_config.cfg', encoding='utf8')
print(cf.sections())
print(cf.options('log_settings'))
cc = cf.get('log_settings', 'log_path')
dd = __file__
print(type(cc))
print(type(dd))
print(cc)
print(dd)
