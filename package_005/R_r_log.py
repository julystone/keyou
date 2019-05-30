import logging
import time


class Mylog:
    def __new__(cls):
        my_log = logging.getLogger('Keyou')
        my_log.setLevel('DEBUG')

        my_ls = logging.StreamHandler()
        my_ls.setLevel('WARNING')
        my_lf = logging.FileHandler(f"{time.strftime('log_%y_%m_%d_%H', time.localtime())}.log", encoding='utf8')
        my_lf.setLevel('DEBUG')

        format = '%(asctime)s | %(process)s | [%(filename)s-->line:%(lineno)d] | %(levelname)-5s: %(message)s'
        my_format = logging.Formatter(format)

        my_ls.setFormatter(my_format)
        my_lf.setFormatter(my_format)

        my_log.addHandler(my_ls)
        my_log.addHandler(my_lf)

        return my_log


if __name__ == '__main__':
    my_log = Mylog()
    my_log.debug('debug')
    my_log.info('info')
    my_log.warning('warning')
    my_log.error('error')
    my_log.critical('critical')
