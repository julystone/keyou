# -*- coding: utf-8 -*-
# @File   :   s_concat.py.py
# @Author :   julystone
# @Date   :   2019/9/9 17:42
# @Email  :   july401@qq.com
import re

string_pattern = r"\=([\s\S]*)\|"

dest = open("./destFile.txt", "r", encoding="utf-8").readlines()

source = open("./sourceFile.txt", "r", encoding="utf-8").readlines()

assert source.__len__() == dest.__len__()

with open("./out.txt", "w+", encoding="utf-8") as f:
    for index in range(source.__len__()):
        words = re.search(string_pattern, source[index]).group(1)

        insert_pos = re.search(string_pattern, dest[index]).span()[1]
        new_list = list(dest[index])
        new_list.insert(insert_pos, words + "|")
        str_2 = "".join(new_list)
        f.write(str_2)
