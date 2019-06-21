import random


# 1、根据你输入的数据，来进行判断学生的成绩。输入数据函数：input()60分以下打印不及格，60-80打印 成绩良好， 80-100打印成绩优秀
def first_ans():
    grades = int(input("Plz input ur grades:\n"))
    while not (grades >= 0 and grades <= 100):
        grades = int(input("Err input, a grade between 0~100 is expected\nPlz input ur grades:\n"))
    if grades < 60:
        response = "不及格"
    elif grades >= 60 and grades < 80:
        response = "成绩良好"
    else:
        response = "成绩优秀"

    print("你本次考试结果为：%s" % response)


# 2、一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格。
def second_ans():
    Buy_price = int(input("请输入付款金额：\n"))
    Discount = 0 if Buy_price < 50 else (0.2 if Buy_price > 100 else 0.1)
    print("您可享受%s%%的折扣\n您的最终价格为：%s" % ((Discount * 100), (Buy_price * (1 - Discount))))


# 3、输入一个数，判断一个数n能同时被3和5整除，能整除打印   ：666    不能整数 打印 ： 一点也不6
def third_ans():
    Test_number = int(input("请输入一个数：\n"))
    print("666") if Test_number % 15 == 0 else print("一点也不6")


# 4、一个 5 位数，判断它是不是回文数。即 12321 是回文数，个位与万位相同，十位与千位相同。 根据判断打印出相关信息。01210
def forth_ans():
    flag = 1
    str_test = input("输入回文数：")
    # print(len(str_test))
    for i in range(0, int(len(str_test) / 2)):
        if list(str_test)[i] != list(str_test)[-1 - i]:
            flag = 0
            break
    print("是回文数") if flag else print("不是回文数")


# 5、利用random函数生成随机整数，从1-9取出来。然后输入一个数字，来猜，如果大于，则打印大于随机数。小了，则打印小于随机数。如果相等，则打印等于随机数
def fifth_ans():
    t = random.randint(1, 9)
    p = eval(input("Plz input ur int number:\n"))
    print("相等！") if t == p else (print("大于随机数%d~" % t) if p > t else print("小于随机数%d~" % t))


# 6、使用if语句完成剪刀石头布游戏，提示：提示用户输入要出的拳 —— 石头（1）／剪刀（2）／布（3）电脑随机出拳比较胜负，显示用户胜、负还是平局。
def sixth_ans():
    while (1):
        Dic = {1: "石头", 2: "剪刀", 3: "布"}
        res = {0: "平局", 1: "胜利", 2: "输了"}
        pc_choice = random.randint(1, 3)
        player_choice = eval(input("请输入要出的拳 —— 石头（1）／剪刀（2）／布（3）"))
        while player_choice not in [1, 2, 3]:
            player_choice = int(input("输入错误\n请输入要出的拳 —— 石头（1）／剪刀（2）／布（3）"))
        if player_choice == pc_choice:
            max_n = 0
        elif player_choice == 1:
            if pc_choice == 2:
                result = 1
            else:
                result = 2
        elif player_choice == 2:
            if pc_choice == 3:
                result = 1
            else:
                result = 2
        else:
            if pc_choice == 1:
                result = 1
            else:
                result = 2
        print("您出了{0}, 电脑出的{1}\n{0}对{1}\t结果为：{2}".format(Dic.get(player_choice), Dic.get(pc_choice), res.get(result)))
        print("是否退出？")
        if (input("C键退出") == "C" or "c"):
            break


if __name__ == "__main__":
    # first_ans()
    # second_ans()
    # third_ans()
    # forth_ans()
    # fifth_ans()
    sixth_ans()
