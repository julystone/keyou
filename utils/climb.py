# @File   :   climb.py
# @Author :   July401
# @Date   :   2019/8/1
# @Email  :   july401@qq.com

import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Time Used:{end - start}")

    return wrapper


@timer
def common():
    for i in range(10000000):
        pass


def climb_1(n):
    def _climb_1(n):
        global dict_t
        if n not in dict_t.keys():
            dict_t[n - 1] = _climb_1(n - 1)
            dict_t[n - 2] = _climb_1(n - 2)
            dict_t[n] = dict_t[n - 1] + dict_t[n - 2]
        return dict_t[n]

    return _climb_1(n)


@timer
def climb_2(n):
    def _climb_2(n):  # 速度非常慢
        if n not in [1, 2]:
            return _climb_2(n - 1) + _climb_2(n - 2)
        else:
            return n

    return _climb_2(n)


def climb_2a(steps):
    dp = ["inf"] * (steps + 1)
    for i in range(1, steps + 1):
        if i not in [1, 2]:
            dp[i] = dp[i - 1] + dp[i - 2]
        else:
            dp[i] = i
    return dp[-1]


@functools.lru_cache(3)
def climb_3(n):
    if n not in [1, 2]:
        return climb_3(n - 1) + climb_3(n - 2)
    else:
        return n


# @timer
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
    # common()
    steps = 30
    dict_t = {1: 1, 2: 2}  # 给方案一特地设定的局部变量
    print(climb_1(steps))
    # print(climb_2(steps))  # 速度非常慢
    print(climb_2a(steps))
    print(climb_3(steps))
    print(climb_4(steps))
