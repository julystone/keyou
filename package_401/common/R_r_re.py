# @File   :   R_r_re.py
# @Author :   July401
# @Date   :   2019/6/22
# @Email  :   july401@qq.com

import configparser
import re

from package_401.common.R_r_config import my_config


class ParmTemp:
    # 用来存储临时变量
    pass


class MyRegex:
    @staticmethod
    def my_replace(string, content=None, split='#', class_temp=None):
        while split in string:
            pattern = f"{split}(.+?){split}"
            try:
                arg = re.search(pattern, string).group(1)
                word = my_config.get('account', arg)
            except configparser.NoOptionError:
                try:
                    word = content if content is not None else getattr(ParmTemp, arg)
                except AttributeError:
                    word = content if content is not None else getattr(class_temp, arg)
            string = re.sub(pattern, word, string, count=1)
        return string

    @staticmethod
    def my_find(string, pattern):
        return re.search(pattern, string).group(1)


myRex = MyRegex()

if __name__ == '__main__':
    list = ['123', None, '2+3']
    for i in list:
        try:
            s = eval(i)
        except TypeError as e:
            s = None
        print(s)
