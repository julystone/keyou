from math import floor
from math import ceil
import re
import time


def max_min(amount_min, amount_max, e = 1):
    # e为敏感参数 默认为
    # e = -1
    burden = amount_max - amount_min
    temp = burden
    while temp > 1:
        e += 1
        temp /= 40
    amount_max_temp = ceil(amount_max / pow(40, e-1)) * pow(40, e-1)
    amount_min_temp = floor(amount_min / pow(40, e-1)) * pow(40, e-1)
    return amount_min_temp, amount_max_temp


def try_except_else_finally():
    try:
        2/0
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


def xing_ps(a,b,c):
    print(a,b,c)


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
            if B[n:n+step] == ''.join(temp):
                n += step
            elif A[m:m+step] == ''.join(temp):
                m += step
            else:
                return False
            temp = []
            step = 0
    return True

if __name__ == '__main__':
    pass
    # s = time.strftime('%m%d%H', time.localtime())
    # print(s)
    print(pinjie())