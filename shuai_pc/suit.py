# -*- coding: utf-8 -*-
# @File   :   suit.py
# @Author :   julystone
# @Date   :   2019/11/20 15:51
# @Email  :   july401@qq.com


li = [1, 1, -2, -4, 5, 6, -1, 5, 6, 1, 6]
li_new = []
sum = li[0]
for num, item in enumerate(li[:-1]):
    if li[num] * li[num + 1] >= 0:
        sum += li[num + 1]
    else:
        li_new.append(sum)
        sum = li[num + 1]

li_new.append(sum)

print(li_new)


print(max(li_new), li_new.index(max(li_new)))


for num, item in enumerate(li_new):
