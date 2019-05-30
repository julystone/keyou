# 1.什么是类？什么是对象？
# 类是具有相同属性和服务的一组对象的集合
# 比如 男人、程序员
# 对象是系统中用来描述客观事物的一个实体，是构成系统的一个基本单位
# 比如 木森
#
#
# 2.类由哪几部分构成？
#  类由 属性、方法组成
# 属性就是类的变量
# 方法就是类里定义的函数
#
#
# 3.实例方法中的self代表什么？
# self 指实例本身  在类外面，新建了实例后，调用实例方法self是自动传入的第一个变量
#
#
# 4.类中__init__方法的作用？
# 初始化函数，新建实例时，第一个就会执行的方法
#
#
# 5.定义一个手机类，
#
# 有属性（打电话，发短信，价格，品牌，型号），
#
# 1、请自己分辨哪些应该定义成类属性，哪些应该定义成实例属性，
#
# 2、有一个设定闹钟的方法，调用该方法后，会提示闹钟已设定好，
#
# 3、有一个查看手机信息的方法，调用该方法后，会显示手机的型号和手机的品牌


class home16thMay:

    class mobile:

        call = '打电话'
        message = '发短信'

        def __init__(self, price = 1000, brand = 'XiaoMi', modelnumber = 'Note'):
            self.price = price
            self.brand = brand
            self.modelnumber = modelnumber

        def setClock(self):
            print("The clock has been set~")

        def checkInfo(self):
            print("该手机的品牌为：{}\n该手机的型号为：{}".format(self.brand, self.modelnumber))


if __name__ == '__main__':
    xiaomiNote = home16thMay().mobile()
    huaweiP30 = home16thMay().mobile(4460, 'Huawei', 'P30')

    huaweiP30.setClock()
    huaweiP30.checkInfo()
    print('-----------------------------')
    xiaomiNote.setClock()
    xiaomiNote.checkInfo()
