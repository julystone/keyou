# @File   :   R_r_config.py.py
# @Author :   July401
# @Date   :   2019/6/3
# @Email  :   july401@qq.com

import configparser
from collections import namedtuple


class Config_data:
    def decorate(self, filename='july_config.cfg'):
        cf = configparser.ConfigParser()
        cf.read(filename, encoding='utf8')
        sections_all = []
        for section_one in cf.sections():
            option_all = []
            for option_one in cf.options(section_one):
                option_all.append(cf.get(section_one, option_one))
            option_tuple = namedtuple(section_one, cf.options(section_one))
            option_tuple_obj = option_tuple(*option_all)
            sections_all.append(option_tuple_obj)
        section_tuple = namedtuple('result', cf.sections())
        section_tuple_obj = section_tuple(*sections_all)
        return section_tuple_obj


my_config = Config_data().decorate()