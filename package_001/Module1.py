import os, random

# 四、对第四次作业的石头剪刀布游戏升级，游戏一轮出拳后进入下一轮，可以手动结束游戏，
# 手动结束游戏后，打印本次游戏的胜率（胜利的把数除以玩的总把数）  
# 提示：（想办法记录一下计算胜率需要的数据，然后就可以算出结果）


def forth_ans(times):
    Sumup = [0,0,0]
    Dic = {1:"石头",2:"剪刀",3:"布"}
    Res = {0:"平局",1:"胜利",2:"输了"}
    while 1:
        pc_choice = random.randint(1,3)
        player_choice_init = input("请输入要出的拳：\n石头【1】  剪刀【2】  布【3】")
        while player_choice_init not in ["1","2","3"]:
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
        times -= 1
        print(times)
        if times == 0:
            print("""
***************************
*****您一共玩了\t{0}次
*****胜\t\t{1}局
*****败\t\t{2}局
*****平\t\t{3}局
*****总胜率为：\t{4:.2f}%
***************************
""".format(Sumup[0]+Sumup[1]+Sumup[2],Sumup[1],Sumup[2],Sumup[0],100*Sumup[1]/(Sumup[0]+Sumup[1]+Sumup[2])))
            break
        os.system("cls")


if __name__ == '__main__':
    forth_ans(2)
