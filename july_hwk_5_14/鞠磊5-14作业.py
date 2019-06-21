import random


class hmwk_5_14:

    # 1、请写出已经学过的python中的关键字？
    # and 	del 	from 	not 	while 	as 	elif
    # global 	or 	with 	assert 	else 	if 	pass
    # break     except 	import 	print 	class
    # in 	raise 	continue 	finally  	return 	def
    # for 	try
    #
    # 2、在异常中，try关键字下的块语句、except下的块语句、else下的块语句、finally下的块语句执行逻辑是什么？
    # try:
    #       块语句发生了异常，异常会被捕获
    # except：
    #       与try一起使用，若语句发生了该类或者它的子类异常，则执行except块语句；
    #       但是如果发生的不是该类或子类异常，那也捕获不到，不执行except块语句
    # else：
    #       与try - except一起使用，若语句未发生任何异常，则执行else
    # finally:
    #       在有try的前提下，非常独立，可以直接使用。不论try后面什么结果，一定会执行finally后的语句

    # 3、当前有个程序，运行起来会提醒用户输入文件名，然后打开（r模式打开）读取内容，打印出来，不存在打开文件会报错，请用捕获改异常，让用户重新输入，
    def read_txt(self):
        filename = input('Plz input the file name you want to read:')
        try:
            f = open(filename, 'r')
            print('The content is: ')
            for i in f.readlines():
                print(i.strip('\n'))
            # print(i for i in f.readlines())
        except FileNotFoundError as err:
            print('File not found, plz check ur word and input again...Below is the origin Err\n{}'.format(err))

    # 4.编写如下程序
    # 优化剪刀石头布游戏程序
    # a.提示用户输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
    # b.电脑随机出拳
    # c.比较胜负，显示用户胜、负还是平局

    # 新需求：
    # d.使用捕获异常的方式，来处理用户输入无效数据的情况
    # e.多次进行游戏，可以让用户选择退出游戏，退出后需要显示胜率
    # 扩展(不要求提交)
    # f.当程序结束之后，要求下一次运行程序能够获取用户历史胜负情况
    # h.如果使用文件保存用户历史胜负数据，需要使用异常来处理文件不存在的情况和实现程序结束后自动关闭文件的功能
    def forth_ans(self):
        # 初始化，将history.txt中历史数据读入Sumup[]中，若不存在文件，则重设为[0, 0, 0]
        Sumup = [0, 0, 0]
        try:
            fp = open('history.txt', 'r', encoding='utf-8')
            temp = fp.readlines()
            for i in range(0, 3):
                Sumup[i] = int(temp[0].split('\'')[2 * i + 1])
        except FileNotFoundError as e:
            print("Attention: File not exist, aft the game ending, a new 'history.txt' will be created locally")
        print(Sumup)

        Dic = {1: "石头", 2: "剪刀", 3: "布"}
        Res = {0: "平局", 1: "胜利", 2: "输了"}
        while 1:
            try:
                player_choice_init = input("请输入要出的拳：\n石头【1】  剪刀【2】  布【3】")
                if player_choice_init not in ["1", "2", "3"]:
                    raise TypeError
            except (ValueError, TypeError) as Err:
                print('出错了，必须是[1,2,3]区间的\n')
                continue
            pc_choice = random.randint(1, 3)
            # while player_choice_init not in ["1","2","3"]:
            #     player_choice_init = input("输入错误\n请输入要出的拳：\n石头【1】  剪刀【2】  布【3】")
            player_choice = int(player_choice_init)
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
            if input("\n\n回车退出游戏，任意键继续游戏") == '':
                print("""
***************************
*****您一共玩了\t{}次
*****平\t\t{}局
*****胜\t\t{}局
*****败\t\t{}局
*****总胜率为：\t{:.2%}
***************************
""".format(Sumup[0] + Sumup[1] + Sumup[2], Sumup[0], Sumup[1], Sumup[2], Sumup[1] / (Sumup[0] + Sumup[1] + Sumup[2])))

                # 记录保存重新写入history.txt，若不存在会创建
                with open('history.txt', 'w', encoding='utf-8') as f:
                    f.write("平局：'{}', 胜局：'{}', 败局：'{}'".format(Sumup[0], Sumup[1], Sumup[2]))
                break


if __name__ == '__main__':
    home = hmwk_5_14()
    home.read_txt()

    print("-------------------------------------")
    home.forth_ans()

    print("-------------------------------------")
