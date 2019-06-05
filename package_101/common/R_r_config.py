# @File   :   R_r_config.py.py
# @Author :   July401
# @Date   :   2019/6/3
# @Email  :   july401@qq.com

from configparser import ConfigParser


# class Config_data:
#     def decorate(self):
#         cf = configparser.ConfigParser()
#         cf.read(r'C:\Users\Administrator\PycharmProjects\keyou\package_101\config', encoding='utf8')
#         sections_all = []
#         for section_one in cf.sections():
#             option_all = []
#             for option_one in cf.options(section_one):
#                 option_all.append(cf.get(section_one, option_one))
#             option_tuple = namedtuple(section_one, cf.options(section_one))
#             option_tuple_obj = option_tuple(*option_all)
#             sections_all.append(option_tuple_obj)
#         section_tuple = namedtuple('result', cf.sections())
#         section_tuple_obj = section_tuple(*sections_all)
#         return section_tuple_obj
class ReadConfig(ConfigParser):
    def __init__(self):
        super().__init__()
        self.read(r'C:\Users\Administrator\PycharmProjects\keyou\package_101\config\july_config.cfg', encoding='utf8')


my_config = ReadConfig()
