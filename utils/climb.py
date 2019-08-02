# @File   :   climb.py
# @Author :   July401
# @Date   :   2019/8/1
# @Email  :   july401@qq.com

import functools


def climb_1(n):
    global dict_t
    if n not in dict_t.keys():
        dict_t[n - 1] = climb_1(n - 1)
        dict_t[n - 2] = climb_1(n - 2)
        dict_t[n] = dict_t[n - 1] + dict_t[n - 2]
    return dict_t[n]


def climb_2(n):  # 速度非常慢
    if n not in [1, 2]:
        return climb_2(n - 1) + climb_2(n - 2)
    else:
        return n


@functools.lru_cache(3)
def climb_3(n):
    if n not in [1, 2]:
        return climb_3(n - 1) + climb_3(n - 2)
    else:
        return n


def climb_4(n):
    def inner():
        (a, b) = (1, 2)
        yield a
        yield b
        while 1:
            yield (a + b)
            (a, b) = (b, a + b)

    bo = inner()
    for _ in range(n):
        s = next(bo)
    return s


if __name__ == '__main__':
    dict_t = {1: 1, 2: 2}  # 给方案一特地设定的局部变量
    print(climb_1(100))
    # print(climb_2(100)) # 速度非常慢
    print(climb_3(100))
    print(climb_4(100))
