# -*- coding: utf-8 -*-
# @File   :   default_dict.py
# @Author :   julystone
# @Date   :   2019/9/2 16:40
# @Email  :   july401@qq.com


from collections import defaultdict, deque, Counter

a = deque()
a.append(1)
a.append(3)
a.append(2)
a.pop()
print(a)





class MyDict:
    pass


dict1 = defaultdict(MyDict)
dict2 = defaultdict(set)
dict3 = defaultdict(str)
dict4 = defaultdict(list)
dict1[2] = 'two'

print(dict1[1])
print(dict2[1])
print(dict3[1])
print(dict4[1])


c = Counter('abracadabra')

print(c.most_common(3))
