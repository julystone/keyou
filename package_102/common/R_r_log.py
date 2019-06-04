import logging
import time
from package_102.common.R_r_config import my_config


class Mylog:
    def __new__(cls):
        name = my_config.get('log', 'name')
        ls_level = my_config.get('log', 'ls_level')
        fs_level = my_config.get('log', 'fs_level')
        log_path = my_config.get('log', 'log_path')

        my_log = logging.getLogger(name)
        my_log.setLevel('DEBUG')

        my_ls = logging.StreamHandler()
        my_ls.setLevel(ls_level)
        my_lf = logging.FileHandler(f"{log_path}{time.strftime('log_%y_%m_%d_%H', time.localtime())}.log",
                                    encoding='utf8')
        my_lf.setLevel(fs_level)

        format = '%(asctime)s | %(process)s | [%(filename)s-->line:%(lineno)d] | %(levelname)-5s: %(message)s'
        my_format = logging.Formatter(format)

        my_ls.setFormatter(my_format)
        my_lf.setFormatter(my_format)

        my_log.addHandler(my_ls)
        my_log.addHandler(my_lf)

        return my_log


my_log = Mylog()
