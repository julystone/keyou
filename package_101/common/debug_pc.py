# @File   :   Pds_Pc.py
# @Author :   July401
# @Date   :   2019/5/30
# @Email  :   july401@qq.com

import configparser

cf = configparser.ConfigParser()
cf.read(r'C:\Users\Administrator\PycharmProjects\keyou\package_101\config\july_config.cfg')
res = cf.get('excel_settings', 'sheet_name')
print(res)
