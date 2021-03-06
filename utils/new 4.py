import csv
import itertools as it
import random
import re

import yaml
from math import ceil
from math import floor


# import pandas as pd


def max_min(min_n, max_n, e=0):
    # e为敏感系数
    temp = max_n - min_n
    while temp > 1:
        e += 1
        temp /= 40
    max_rounded = ceil(max_n / pow(40, e - 1)) * pow(40, e - 1)
    min_rounded = floor(min_n / pow(40, e - 1)) * pow(40, e - 1)
    return min_rounded, max_rounded


def try_except_else_finally():
    try:
        2 / 0
    except:
        print("except")
    else:
        print("else")
    finally:
        print("finally")


def exception_practise():
    i = 1
    while i:
        try:
            player_choice_init = input("请输入要出的拳：\n石头【1】  剪刀【2】  布【3】")
            if player_choice_init not in ["1", "2", "3"]:
                raise TypeError
            break
        except (ValueError, TypeError):
            print('出错了，必须是[1,2,3]区间的\n')

        # i -= 1


def re_ps2():
    str1 = r'everasdqgfeverqasdaaaeeeqqeveracaeeewqaccc'
    regex = r'ever((?!ever).)*ccc'
    res = re.search(regex, str1).group()
    print(res)


def xl_ps():
    pattern = re.compile(r"ever((?!ever).)*ccc")
    str1 = u'everasdqgfeverqasdaaaeeeqqeveracaeeewqaccc'
    print(pattern.search(str1))


def xing_ps(a, b, c):
    print(a, b, c)


def pingjie_pc():
    a = 'asdf'
    b = 'axzxcv'
    c = 'axaszxdfcv'
    m = 0
    n = 0
    for i in c:
        if b[n] == i:
            n += 1
        elif a[m] == i:
            m += 1
        else:
            break
    flag = 1 if m == len(a) and n == len(b) else 0
    print(flag)


def pingjie_pc2():
    a = 'asdf'
    b = 'axzxcv'
    c = 'axaszxdfcv'
    m = 0
    n = 0
    for i in c:
        if b[n] == i:
            n += 1
        elif a[m] == i:
            m += 1
        else:
            return False
    return True


def pinjie():
    A = "asdf"
    B = "axazxcv"

    S = "axasazxdfcv"
    m = 0
    n = 0
    temp = []
    step = 0
    A = A + ' '
    B = B + ' '
    # 预处理一下，防止下标越界
    for i in S:
        temp += i
        step += 1
        if B[n] == A[m] == i:
            continue
        else:
            if B[n:n + step] == ''.join(temp):
                n += step
            elif A[m:m + step] == ''.join(temp):
                m += step
            else:
                return False
            temp = []
            step = 0
    return True


def csv_pc():
    with open("测试成绩统计.csv", "r+") as file1:
        file1reader = csv.reader(file1)
        file1writer = csv.writer(file1)
        header = next(file1reader)
        for row_list in file1reader:
            a = float(row_list[1]) + float(row_list[2]) + float(row_list[3]) + float(row_list[4]) + float(row_list[5]) \
                + float(row_list[6]) + float(row_list[7]) + float(row_list[8]) + float(row_list[9])
            res = str(a / 9)
            row_list.append(res)
            pass
            file1writer.writerow(row_list[10])


def csv_pc2():
    with open("测试成绩统计.csv", "r+", encoding='utf-8') as file1:
        file1reader = csv.reader(file1)
        file1writer = csv.writer(file1)
        file1writer['avg'] = ' '
        for i in file1reader:
            if i[1] == '1':
                continue
            sum = 0
            for y in i:
                sum += float(y)
            avg = sum / 9
            # print(avg)
            i.append(avg)
            print(i)
            file1writer.writerow(i[10])


# def pd_pc():
#     res = pd.read_csv('测试成绩统计_back.csv', encoding='gb2312')
#     res.insert(res.shape[1], 'avg', None)
#     for x in range(res.shape[0]):
#         sum = 0
#         for y in range(res.shape[1] - 2):
#             sum += res.iloc[x][y + 1]
#         avg = sum / 9
#         res.loc[x, 'avg'] = round(avg, 2)
#     res.to_csv('测试成绩统计2.csv', index=False)


def one_number(word):
    if '|' in word:
        temp = re.split("[-|]", word)
        begin = int(temp[0] + temp[1])
        end = int(temp[0] + temp[2])
        return random.randint(begin, end)


def one_number(number):
    head = '139'
    for _ in range(number - len(head)):
        head += str(random.randint(0, 9))
    return int(head)


def re_pc_22():
    p = r"\${(.+?)}"
    data = """{"mobilephone":"${phone}"}"""
    key = re.search(p, data).group()
    # value = re.search(p, data).group(1)
    print(key)


def random_pc():
    temp = check_times = 0
    number = ""
    random_list = [1, 2, 3, 45, 5]
    while 1:
        for i in random_list:
            number += str(i)
        if int(number) > temp:
            temp = int(number)
            check_times = 0
        else:
            check_times += 1
        random.shuffle(random_list)
        number = ""
        if check_times == 100:
            break
    print(temp)


def random_pc2():
    aa = [1, 2, 3, 45, 5]
    bb = aa
    e = 0
    aa.sort()
    cc = []
    f = aa[-1]
    while f > 1:
        f /= 10
        e += 1
    print(e)
    for item in aa:
        bur = 2 - str(item).__len__()
        if bur > 0:
            item *= 10 ** bur
        cc.append(item)
    print(aa)
    print(cc)
    cc.sort()


def random_pc3():
    aa = [5, 2, 3, 54, 4]
    bb = []
    res = ""
    for item in aa:
        bb.append(str(item))
    bb.sort()
    for item in bb:
        res += item
    print(int(res))
    print(bb)


from functools import cmp_to_key


def xy_cmp(x, y):
    if x + y > y + x:
        return 1
    elif x + y < y + x:
        return -1
    else:
        return 0


def number_cmp(li):
    li = list(map(str, li))
    li.sort(key=cmp_to_key(xy_cmp))
    # li.sort()
    return ''.join(li)


class CountIter:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.x = -1
        return self


def lambda_pc():
    a = 1
    b = 2
    c = 3
    add = lambda x: (x == x + 1)
    print(add(a))
    a = add(a)
    print(a)


from suds import client


def web_pc():
    web_service = client.Client(url='http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl')
    web_service = client.Client(
        url='http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl')
    print(web_service)


def interview_pc():
    a = [8, 9, 10, 11, 12, 13, 14, 15]
    b = a.insert(1, 'w')
    print(a)
    print(b)


def calcu_pc():
    with open("history.txt", "r", encoding="utf-8") as f1:
        history = f1.readlines()
        for lineNo in range(len(history)):
            print(f"No.{lineNo + 1} result: {history[lineNo]}")
        if 'lineNo' not in dir():
            print("Not even one cal recorded")
    # string = " 10.. # 012 #-3#11.2#9"  # test data
    string = input("enter ur string:")
    list_temp = string.split("#")
    print(list_temp)
    temp = 1
    for number in list_temp:
        try:
            if eval(number) == 0:
                continue
            temp *= eval(number)
        except:
            print(f"wrong input: {number} is not a number")
    with open("history.txt", "a+", encoding="utf-8") as f2:
        f2.writelines(str(temp % 23) + '\n')


def eval_pc():
    i = 12
    j = 13
    answer = 0
    loc = locals()
    exec("answer=i*j")
    print("Answer is %s" % answer)


def test2():
    a = 23
    b = 56
    loc = locals()
    for i in [1, 2, 3]:
        exec(f"c{i} = a + b + {i}", loc)
        exec(f"c{i} = loc['c{i}']")
        exec(f"print(c{i})")


def in_pc():
    happy = 11
    sad = 12
    print('happy' in dir())
    print('happy' in locals())


from collections import Counter


def fun(tup):
    return tup[1]


def inst_pc(list2sort, N):
    # 直接用Counter
    print(Counter(list2sort))

    temp = {}
    for item in list2sort:
        if item not in temp.keys():
            temp[item] = 1
        else:
            temp[item] += 1

    res = sorted(temp.items(), key=fun, reverse=True)
    i = 1
    while N > 0:
        out = res.pop(0)
        print(f"第{i}个重复数字为：{out[0]}，重复了{out[1]}次")
        N -= 1
        i += 1


def inst_pc1(list2sort, N):
    temp = {}
    for i, j in it.groupby(sorted(list2sort)):
        temp[i] = len(list(j))
    res = sorted(temp.items(), key=fun, reverse=True)

    for key, value in res:
        print(key, value)
        N -= 1
        if N == 0:
            break


def login():
    passwd = {"july": "123"}
    time = 0
    s = input("Plz input ur username:".center(60, "*"))
    while s not in passwd.keys():
        print("Username wrong or not exist.".upper())
        s = input("Plz input ur username again:".center(60, "*"))
    while input("Plz input ur password:".center(60, "*")) != passwd[s]:
        time += 1
        if time > 3:
            print("You've inputed too much wrong password, System Aborted.".upper())
            return
        print(f"Password incorrect. You still have {4 - time} time to input".upper())
    print("Welcome".center(60, "*"))


import os


def file_path():
    print(os.path.abspath("./"))
    print(os.listdir("./"))
    for dir in os.listdir("./"):
        if os.path.isdir(dir):
            print("1")


def inter_pc():
    for i, j in it.groupby(sorted("aavbvcc")):
        print(i, list(j))


import functools


@functools.lru_cache(10)
def climb_stairs2(n):
    if n != 1 and n != 2:
        return climb_stairs2(n - 1) + climb_stairs2(n - 2)
    elif n == 2:
        return 2
    elif n == 1:
        return 1


def foo():
    print("starting...")
    while True:
        for _ in range(5):
            yield _


def climb_stairs3(n):
    def fibo():
        (a, b, c) = (1, 2, 4)
        while 1:
            yield a + b + c
            (a, b, c) = (b, c, a + b + c)

    k = fibo()
    for _ in range(4, n, 1):
        # print(next(k))
        print(f"{_}层楼梯，有{next(k)}种方式")


def ft_pc():
    def add_raw(a, b, c, d):
        return a + b + c + d

    add_all = functools.partial(add_raw, 1, 2, 3, 4)
    print(add_all())


def gene_dic_pc():
    dict1 = {a: a ** 2 for a in range(0, 10, 2)}
    print(dict1)


def fibo_pc(n):
    def inner():
        (a, b) = (1, 2)
        while 1:
            yield a + b
            (a, b) = (b, a + b)

    g = inner()
    for _ in range(4, 101, 1):
        print(f"第{_}：{next(g)}")


def checkIfInfoLine(string):
    pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} "
    return re.search(pattern, string)


def intergalTrans(inter):
    inter = inter.lower()
    special_symbol = ["w", "万"]
    for symbol in special_symbol:
        if symbol in inter:
            raw_int = inter.split(symbol)[0]
            if "." in raw_int:
                return float(raw_int) * 10000
            raw_float = inter.split(symbol)[1]
            return float(raw_int + "." + raw_float) * 10000


def yaml_read():
    YAML_PATH = "./config.yaml"
    with open(YAML_PATH, 'r', encoding='utf-8') as f:
        conf = yaml.safe_load(f)
        print(conf['txt']['path'])


def split_pc():
    sample = r"C://dasdswdq//cqcno\bvwsedco\x.txt"
    res = sample.split("//|/")[-1]
    res = re.split(r"//|/|\\", sample)
    print(res)


def sort_list(li):
    for i in range(li.__len__() - 1):
        for j in range(i, li.__len__()):
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]
    return li


def find_pc():
    s1 = "abcdefg"
    s2 = "def"
    print(s1[1:-1])
    print(s1.find(s2))
    print("%s_%s" % (s1, s2))


#
# class inter_pattern:
#
#     def __init__(self, N):
#         self.pat = [[0 for i in range(N)] for j in range(N)]
#         self.N = N
#         # self.direction = {"left": (0, 1), "down": (1, 0), "right": (0, -1), "up": (-1, 0)}
#         self.direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#
#     def cal_dir(self, row, column, direction):
#         try: self.pat[row + direction[0]][column + direction[1]] == 0
#         except IndexError: return direction["down"]
#
#     def run(self):
#         for data in range(1, self.N * self.N + 1):
#
#     def climb_4(self, n):
#         def inner():
#             (a, b) = (0, 0)
#             yield (a, b)
#             d = self.direction[0]
#             while 1:
#                 try:
#                     self.pat[a + d[0]][b + d[1]] = n
#                 except IndexError:
#                     d = self.direction
#                 yield (a, b)
#
#         bo = inner()
#         for _ in range(n):
#             s = next(bo)
#         return s
class tuple(tuple):
    def __add__(self, other):
        new_tuple = []
        for index in range(len(self)):
            new_tuple.append(self[index] + other[index])
        return tuple(new_tuple)

    def __sub__(self, other):
        new_tuple = []
        for index in range(len(self)):
            new_tuple.append(self[index] - other[index])
        return tuple(new_tuple)


def rotate(N):
    table = [[0 for i in range(N)] for j in range(N)]
    (i, j, k) = (0, 0, 0)
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    length = len(str(N * N))
    li = [f"{i:0{length}d}" for i in range(1, N * N + 1)]
    # zz1 = (i, j)
    # zz1 = MyTuple(zz1)
    for _ in li:
        try:
            if i < 0 or j < 0 or table[i][j] != 0:
                raise IndexError
            table[i][j] = _
            (i, j) = (i + direction[k][0], j + direction[k][1])
        except IndexError:
            (i, j) = (i - direction[k][0], j - direction[k][1])
            k += 1
            try:
                (i, j) = (i + direction[k][0], j + direction[k][1])
            except IndexError:
                k = 0
                (i, j) = (i + direction[k][0], j + direction[k][1])
            table[i][j] = _
            (i, j) = (i + direction[k][0], j + direction[k][1])

    for item in table:
        print(item)


def zxc():
    string = "a=1,b=2,c=3"
    string_out = ""
    pattern1 = r".*(?<=\=)"
    pattern2 = r"(?=\=).*"
    for item in string.split(","):
        out = re.sub(pattern1, "123", item)
        print(out)
    print(string)


if __name__ == '__main__':
    # test2()
    # calcu_pc()
    # inst_pc1([1, 2, 3, 4, 5, 6, 1, 3, 5, 6, 2, 1, 3, 1, 5], 4)
    # inst_pc([1, 2, 3, 4, 5, 6, 1, 3, 5, 6, 2, 1, 3, 1, 5], 4)
    # split_pc()
    # print(sort_list([2, 5, 1, 2, 6, 1, 6, 321, 3, 5, 51]))
    # find_pc()inter_pcc
    # rotate(10)
    # zz1 = (1, 2)
    # zz1 = tuple(zz1)
    # zz2 = (3, 4)
    # zz2 = tuple(zz2)
    # zz2 = MyTuple()
    # zz2 = tuple(2, 3)
    # print(zz1 + zz2)
    # print(zz1 + zz2)
    # zxc()
    re_ps2()
    # inter_pc()
    # for i in range(1, 101, 1):
    #     print(f"{i}层楼梯，有{climb_stairs2(i)}种方式")
    # g = fibo_pc(100)
    # h = climb_stairs3(100)
    # for _ in range(50):
    #     print(next(g))
    # print(next(g))
    # print(next(g))
    # print(next(g))
    # print(next(g))
    # print(checkIfInfoLine("aaa"))
    # print(intergalTrans("1万"))
    # yaml_read()
