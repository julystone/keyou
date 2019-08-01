# @File   :   login.py
# @Author :   July401
# @Date   :   2019/7/31
# @Email  :   july401@qq.com
import os


def sys_init():
    account_list = {}
    file_dir = "./account_list.txt"
    if not os.path.exists(file_dir):
        f = open("./account_list.txt", "w", encoding="utf-8")
        f.close()
    with open("./account_list.txt", "r", encoding="utf-8") as f:
        old_list = f.readlines()
        for _ in old_list:
            acc = _.split(',')[0]
            pwd = _.split(',')[1]
            account_list[acc] = pwd
    return account_list


def login(account_list):
    while 1:
        acc = input("请输入账号：")
        pwd = input("请输入密码：")
        if account_list.get(acc) == pwd:
            print("账号密码正确，登陆成功")
            print("欢迎进入图书管理系统".center(28, "-"))
            break
        else:
            print("您输入的账号或者密码不正确，请重新输入")


def register(account_list):
    while 1:
        new_acc = input("请输入新账号：")
        if new_acc in account_list.keys():
            print("该账户已存在")
            continue
        new_pwd = input("请输入密码：")
        new_pwd_2nd = input("请再次确认密码：")
        if new_pwd != new_pwd_2nd:
            print("注册失败，两次输入的密码不一致")
            continue
        # 注册成功
        print("注册成功")
        account_list[new_acc] = new_pwd
        with open("./account_list.txt", "a+", encoding="utf-8") as f:
            f.writelines(f"{new_acc},{new_pwd}")
        break


if __name__ == '__main__':
    account_list = sys_init()
    switch = input("提示：【1】登录、【2】注册")
    if switch == '1':
        login(account_list)
    elif switch == '2':
        register(account_list)
    else:
        print("Wrong Input, Plz Check.")
