import os
import random


class hmwk_4_27():

    # 一、输出99乘法表，结果如下：（提示for循环，格式化输出）
    def first_ans(self):
        for i in range(1, 10):
            for j in range(1, i + 1):
                print("{} * {} = {}".format(i, j, i * j), end='\t')
            print("")

    # 二、for循环对列表中的数据排序：
    # 利用for循环，完成a=[1,7,4,89,34,2]的从小到大排序（不能使用列表的sort方法）：
    def second_ans(self, lista):
        lena = len(lista)
        for i in range(0, lena - 1):
            for j in range(i + 1, lena):
                if lista[i] > lista[j]:
                    lista[i], lista[j] = lista[j], lista[i]
        print(lista)

    # 三、有1 2 3 4 这四个数字，设计程序计算能组成多少个互不相同且无重复数字的3位数？分别是什么？abc （a!=b!=c）
    def third_ans(self, lista):
        times = 0
        for i in range(len(lista)):
            # 首位不能为0
            if lista[i] == 0:
                continue
            listb = lista[:i] + lista[i + 1:]
            for j in range(len(listb)):
                listc = listb[:j] + listb[j + 1:]
                for k in listc:
                    times += 1
                    print("第{}个无重复的数为：\t{}{}{}".format(times, lista[i], listb[j], k))

    # 四、对第四次作业的石头剪刀布游戏升级，游戏一轮出拳后进入下一轮，可以手动结束游戏，
    # 手动结束游戏后，打印本次游戏的胜率（胜利的把数除以玩的总把数）
    # 提示：（想办法记录一下计算胜率需要的数据，然后就可以算出结果）
    def forth_ans(self):
        Sumup = [0, 0, 0]
        Dic = {1: "石头", 2: "剪刀", 3: "布"}
        Res = {0: "平局", 1: "胜利", 2: "输了"}
        while (1):
            pc_choice = random.randint(1, 3)
            player_choice_init = input("请输入要出的拳：\n石头【1】  剪刀【2】  布【3】")
            while player_choice_init not in ["1", "2", "3"]:
                player_choice_init = input("输入错误\n请输入要出的拳：\n石头【1】  剪刀【2】  布【3】")
            player_choice = int(player_choice_init)
            # print("{},{},{}".format(player_choice,pc_choice,player_choice - pc_choice))
            if player_choice == pc_choice:
                result = 0
                Sumup[0] += 1
            elif player_choice - pc_choice == 2 or player_choice - pc_choice == -1:
                result = 1
                Sumup[1] += 1
            else:
                result = 2
                Sumup[2] += 1
            print("""
***************************
*****您：\t{0}
*****电脑：\t{1}
*****结果：\t{2}
***************************
""".format(Dic.get(player_choice), Dic.get(pc_choice), Res.get(result)))
            if input("\n\n回车清屏，任意键取消") == '':
                print("""
***************************
*****您一共玩了\t{0}次
*****胜\t\t{1}局
*****败\t\t{2}局
*****平\t\t{3}局
*****总胜率为：\t{4:.2f}%
***************************
""".format(Sumup[0] + Sumup[1] + Sumup[2], Sumup[1], Sumup[2], Sumup[0],
           100 * Sumup[1] / (Sumup[0] + Sumup[1] + Sumup[2])))
                break
            os.system("cls")

    # 五、图书管理系统功能完善（上课已经实现的功能上进行完善）
    # 说明：每一本图书包含三条信息：图书编号，图书名称，存放位置
    # 添加功能实现：依次输入图书编号  图书名  图书位置进行添加（参考如下）
    # 删除功能实现：输入书名，删除图书。
    # 显示所有书籍：显示出所有书本的信息（分行显示，每行显示一本）
    # （下面两个功能为扩展，有时间可以去做，没时间可以不做）
    # 查询图书的功能、
    # 修改图书信息的功能：
    def checkIfNumOccpd(self, is_in, book_No, book_all):
        # 检查图书ID是否已被占用
        # is_in --"Y"     该书已存在
        #       --"N"     该书不存在
        # return--1:true
        #       --0:false
        flag = 0
        if is_in == "Y":
            if book_No in book_all.keys():
                flag = 1
        elif is_in == "N":
            if book_No not in book_all.keys():
                flag = 1
        return flag

    def checkIfPosOccpd(self, is_occpd, book_Pos, book_all):
        # 检查书架位置是否已被占用
        # is_occpd--"Y"     位置已被占
        #         --"N"     位置尚未空
        # return--1:true
        #       --0:false
        if is_occpd == "Y":
            flag = 0
            for dics in book_all.values():
                if book_Pos == dics.get('book_Pos'):
                    # 如果位置已有书
                    flag = 1
        elif is_occpd == "N":
            flag = 1
            for dics in book_all.values():
                if book_Pos == dics.get('book_Pos'):
                    # 如果位置已有书
                    flag = 0
        return flag

    def fifth_ans(self):
        info = {'july': '111111', 'lemon': '222222'}
        book_all = {}
        while (1):
            # username = input("请输入账号：")
            # password = input("请输入密码：")
            # if username not in info.keys():
            if (0):
                print("账号不存在，请检查并重新输入")
            # elif password != info.get(username):
            elif (0):
                print("密码错误，请检查并重新输入")
            else:
                print("账号密码正确，登录成功")
                print("------欢迎进入图书管理系统------")
                while (1):
                    if input("\n\n回车清屏，任意键取消") == '':
                        os.system("cls")
                    print("""
********************************
********【1】:添加图书
********【2】:修改图书
********【3】:删除图书
********【4】:查询图书
********【5】:退出
********************************
""")
                    num = input("请输入您的选项：")
                    if num == '1':
                        print("#添加图书")
                        book_No = input("请输入图书编号：")
                        book_Name = input("请输入图书名称：")
                        book_Pos = input("请输入图书位置：")
                        if self.checkIfNumOccpd("Y", book_No, book_all):
                            # 如果编号已被占据，则报冲突
                            print("********【Err】图书编号冲突，添加失败")
                            continue
                        if self.checkIfPosOccpd("Y", book_Pos, book_all):
                            # 如果位置已被占据，则报冲突
                            print("********【Err】该位置已被占据，添加失败")
                            continue
                        book = {'book_Name': book_Name, 'book_Pos': book_Pos}
                        book_all[book_No] = book
                        print("********【系统】图书添加成功")
                    elif num == '2':
                        print("#修改图书")
                        book_No = input("请输入图书编号：")
                        if self.checkIfNumOccpd("N", book_No, book_all):
                            # 如果编号不存在，则报错
                            print("********【Err】不存在该图书，无法修改")
                            continue
                        book_Name = input("请输入更改后的图书名称：")
                        book_Pos = input("请输入更改后的图书位置：")
                        if self.checkIfPosOccpd("Y", book_Pos, book_all):
                            # 如果位置已被占据，则报冲突
                            print("********【Err】该位置已被占据，修改失败")
                            continue
                        book = {'book_Name': book_Name, 'book_Pos': book_Pos}
                        book_all[book_No] = book
                        print("********【系统】图书修改成功")
                    elif num == '3':
                        print("#删除图书")
                        book_No = input("请输入图书编号：")
                        if self.checkIfNumOccpd("N", book_No, book_all):
                            # 如果编号不存在，则报错
                            print("********【Err】不存在该图书，无法删除")
                            continue
                        del book_all[book_No]
                        print("********【系统】图书删除成功")
                    elif num == '4':
                        print("#查询图书")
                        # if input("\n\n查询全部【0】，查询单本【1】") == '1':
                        book_No = input("请输入图书编号：")
                        if self.checkIfNumOccpd("N", book_No, book_all):
                            # 如果编号不存在，则报错
                            print("********【Err】不存在该图书")
                            continue
                        print("""********【系统】该书信息如下：\n********【系统】图书名称：{0}\n********【系统】图书位置：{1}""".format(
                            book_all[book_No]["book_Name"], book_all[book_No]["book_Pos"]))
                    elif num == '5':
                        print("#退出")
                        break
                    else:
                        print("输入错误")
                break


# 6、总结前面学习过的所有知识点，画成思维导图
# 思维导图见附件

if __name__ == "__main__":
    home = hmwk_4_27()
    # home.first_ans()
    # home.second_ans([1,7,4,89,34,2])
    home.third_ans([1, 2, 3, 4])
    # home.forth_ans()
    # home.fifth_ans()
