# @File   :   R_r_re.py
# @Author :   July401
# @Date   :   2019/6/22
# @Email  :   july401@qq.com

import re

from package_301.common.R_r_config import my_config


def search(string, content=None, split='#'):
    while split in string:
        pattern = f"{split}(.+?){split}"
        if content is None:
            arg = re.search(pattern, string).group(1)
            word = my_config.get('account', arg)
        else:
            word = content
        string = re.sub(pattern, word, string, count=1)
    return string


if __name__ == '__main__':
    text = 'wwwww.#phone#cva#pwd#scc'
    text2 = search(text)
    print(text2)
