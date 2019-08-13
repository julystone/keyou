def pc_1():
    a = {"A": 1, "B": 2}
    return {key: value for value, key in a.items()}


if __name__ == '__main__':
    res = pc_1()
    print(res)
