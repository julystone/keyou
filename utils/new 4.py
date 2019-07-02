import csv
import random
import re
import time
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
        except (ValueError, TypeError) as Err:
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


def pd_pc():
    res = pd.read_csv('测试成绩统计_back.csv', encoding='gb2312')
    res.insert(res.shape[1], 'avg', None)
    for x in range(res.shape[0]):
        sum = 0
        for y in range(res.shape[1] - 2):
            sum += res.iloc[x][y + 1]
        avg = sum / 9
        res.loc[x, 'avg'] = round(avg, 2)
    res.to_csv('测试成绩统计2.csv', index=False)


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


if __name__ == '__main__':
    pass
    s = time.strftime('%Y%m%d%H', time.localtime())
    # print(s)
    # print(pinjie())
    # csv_pc2()
    # print(max_min(100, 101))
    # tt = one_number("1391254|0000-9999|")
    # print(re_ps2())
    # re_pc_22()
    random_pc3()
    print(number_cmp([5, 2, 3, 54, 4]))
    for i in CountIter(5):
        print(i)
