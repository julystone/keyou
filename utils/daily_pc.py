def pc_1():
    a = {"A": 1, "B": 2}
    return {value: key for key, value in a.items()}


if __name__ == '__main__':
    res = pc_1()
    print(res)
