# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
#
# 实现文字版游戏：坦克大战
# 步骤一：定义TANK类（必做）：
# 1、实现一个BaseTank类（所有Tank的父类）
# BaseTank拥有live属性（这个属性代表Tank是否存活 :  1代表活的，0代表死）
# BaseTank拥有postion属性（这个属性代表Tank的位置，位置随机生成，一共有（1,10）10个位置）
# BeseTank拥有HP属性（代表血量，默认为10）
# BeseTank拥有attck_postion属性（代表攻击位置，位置随机生成，一共有（1,10）10个位置）
# BaesTank拥有一个hit方法，该方法除self外，还接收一个参数other(代表对方Tank)，在该方法中判断，对方攻击位置和自己所在的位置是否一致，如果一致的话，就给自己的HP减1，当HP等于0时，修改live属性（改为死亡状态）
#
# 2、实现一个玩家坦克类，MyTank,继承于BaseTank，该类拥有两个方法。
# move方法：(移动tank位置)调用该方法时，提示玩家输入移动的目标位置，输入完之后，将坦克移动到输入的位置，（输入无效数据，提示用户重新输入，通过异常来处理无效数据）
# Bullet_launch方法：发射子弹，提示玩家输入攻击的目标位置，（输入无效数据，提示用户重新输入，通过异常来处理无效数据）
#
# 3、实现一个电脑坦克类，PCTank,继承于BaseTank，该类拥有两个方法。
# move方法：(移动tank位置) 调用该方法时，随机移动位置（1,10）
# Bullet_launch方法：发射子弹，攻击目标位置随机生成（1,10），
#
# 步骤二：游戏规则逻辑完善（扩展题做，不要求提交）
# 1、启动游戏后，创建一个玩家坦克，一个电脑tank,
# 2、游戏环节（循环，直到有tank死亡才退出循环）
# 1、玩家发生子弹，然后电脑坦克发射子弹，
# 2、玩家判断有没有被电脑击中，电脑判断有没有被玩家击中。
# 3、判断双方坦克是否存活，如果有tank死亡，则宣布存活的一方胜利。都存活则继续游戏。
# 4、玩家移动、电脑移动
import random


class TanKeDaZhan:
    class BaseTank:
        live = 1
        postion = random.randint(1, 10)
        HP = 10
        attack_position = random.randint(1, 10)

        def hit(self, other):
            if self.postion == other.attack_position:
                self.HP -= 1
                print("HITTED! HP:{}".format(self.HP))
            if self.HP == 0:
                self.live -= 1
                self.HP = 10

    class MyTank(BaseTank):
        def move(self):
            while 1:
                try:
                    position = int(input('Ur next pos:'))
                except:
                    print('Input Err, plz input again')
                    continue
                else:
                    break
            self.postion = position

        def Bullet_launch(self):
            while 1:
                try:
                    position = int(input('Ur attack pos:'))
                except:
                    print('Input Err, plz input again')
                    continue
                else:
                    break
            self.attack_position = position

    class PCTank(BaseTank):
        def move(self):
            self.postion = random.randint(1, 10)

        def Bullet_launch(self):
            self.attack_position = random.randint(1, 10)

        def hit(self, other):
            if self.postion == other.attack_position:
                self.HP -= 1

    #
    # 步骤二：游戏规则逻辑完善（扩展题做，不要求提交）
    # 1、启动游戏后，创建一个玩家坦克，一个电脑tank,
    # 2、游戏环节（循环，直到有tank死亡才退出循环）
    # 1、玩家发生子弹，然后电脑坦克发射子弹，
    # 2、玩家判断有没有被电脑击中，电脑判断有没有被玩家击中。
    # 3、判断双方坦克是否存活，如果有tank死亡，则宣布存活的一方胜利。都存活则继续游戏。
    # 4、玩家移动、电脑移动

    def main(self):
        My = self.MyTank()
        PC = self.PCTank()
        while 1:
            My.Bullet_launch()
            PC.Bullet_launch()
            My.hit(PC)
            PC.hit(My)
            if My.live == 0:
                print('You lose..')
                break
            elif PC.live == 0:
                print('You win!')
                break
            else:
                menu_list = ['', 'Current', 'Ur HP:', 'PC HP:', 'Ur live:', '']
                data_list = ['', '    ', My.HP, PC.HP, My.live, '']
                for i in range(len(menu_list)):
                    print("%s" % menu_list[i].center(28 - len(menu_list), ' ') + "%s" % data_list[i])
                # print('Current: \nUr HP:{}\t PC HP:{}\nUr live:{}'.format(My.HP, PC.HP, My.live))
            My.move()
            PC.move()


if __name__ == '__main__':
    zy = TanKeDaZhan()
    zy.main()
