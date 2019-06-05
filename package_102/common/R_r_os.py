# @File   :   R_r_os.py.py
# @Author :   July401
# @Date   :   2019/6/5
# @Email  :   july401@qq.com

import os


class OsRead:
    def readpath(self, filepattern, ifsymbol='True'):
        cur_path = os.path.dirname(os.path.realpath(__file__))
        dest_path = os.path.join(os.path.dirname(cur_path), filepattern + '\\') if ifsymbol else os.path.join(
            os.path.dirname(cur_path), filepattern)
        return dest_path


my_os = OsRead()
res = my_os.readpath('log')
print(res)
