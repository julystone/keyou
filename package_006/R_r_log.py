import logging
import time
from package_006.R_r_config import my_config


class Mylog:
    def __new__(cls):
        logger_name = my_config.log_settings.logger_name
        log_level_stream = my_config.log_settings.log_level_stream
        log_level_file = my_config.log_settings.log_level_file
        log_path = my_config.log_settings.log_path

        my_log = logging.getLogger(logger_name)
        my_log.setLevel('DEBUG')

        my_ls = logging.StreamHandler()
        my_ls.setLevel(log_level_stream)
        my_lf = logging.FileHandler(f"{log_path}\{time.strftime('log_%y_%m_%d_%H', time.localtime())}.log", encoding='utf8')
        my_lf.setLevel(log_level_file)

        format = '%(asctime)s | %(process)s | [%(filename)s-->line:%(lineno)d] | %(levelname)-5s: %(message)s'
        my_format = logging.Formatter(format)

        my_ls.setFormatter(my_format)
        my_lf.setFormatter(my_format)

        my_log.addHandler(my_ls)
        my_log.addHandler(my_lf)

        return my_log


my_log = Mylog()