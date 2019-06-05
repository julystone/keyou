import logging
import time
from package_101.common.R_r_config import my_config


class Mylog:
    def __new__(cls):
        name = my_config.get('log', 'name')
        all_level = my_config.get('log', 'all_level').upper()
        ls_level = my_config.get('log', 'ls_level').upper()
        fs_level = my_config.get('log', 'fs_level').upper()
        path = my_config.get('log', 'path')

        my_log = logging.getLogger(name)
        my_log.setLevel(all_level)

        my_ls = logging.StreamHandler()
        my_ls.setLevel(ls_level)
        my_fs = logging.FileHandler(fr"{path}{time.strftime('log_%y_%m_%d_%H', time.localtime())}.log", encoding='utf8')
        my_fs.setLevel(fs_level)

        format = '%(asctime)s | %(process)s | [%(filename)s-->line:%(lineno)d] | %(levelname)-5s: %(message)s'
        my_format = logging.Formatter(format)

        my_ls.setFormatter(my_format)
        my_fs.setFormatter(my_format)

        my_log.addHandler(my_ls)
        my_log.addHandler(my_fs)

        return my_log


my_log = Mylog()