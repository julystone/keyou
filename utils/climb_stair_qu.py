import functools
from datetime import datetime


def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        print(f"Time used: {start - end}")

    return wrapper


# @timer
def climb_stairs1(n):
    if n not in [1, 2]:
        return climb_stairs1(n - 1) + climb_stairs1(n - 2)
    else:
        return n  # 此处投机取巧，n = 1确实是1种，n = 2 也确实是2种


if __name__ == '__main__':
    for _ in range(1, 101, 1):
        start = datetime.now()
        counts = climb_stairs1(_)
        end = datetime.now()
        print(f"Time used: {end - start}\t{_}\t{counts}")
