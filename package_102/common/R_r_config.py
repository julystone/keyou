# @File   :   R_r_config.py.py
# @Author :   July401
# @Date   :   2019/6/3
# @Email  :   july401@qq.com

import configparser


class Config_data(configparser.ConfigParser):
    def __init__(self):
        super().__init__()
        self.read(r'C:\Users\esunny\PycharmProjects\keyou\package_102\config\config.ini')


my_config = Config_data()
print(my_config.get('log', 'name'))