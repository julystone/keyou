# 1.什么是模块？有什么作用？
# 模块就是一个py文件，导入了这个module后，就可以使用这个py文件里面的方法、类等等




# 2.模块的导入方式有哪几种？
# 有总共5种：
# import dic_2_file                     dic_2_file.main()
# import dic_2_file as jl               jl.main()
# from dic_2_file import main           main()  可以在main后面加逗号，导入多个
# from dic_2_file import main as jl     jl()    可以在main后面加逗号，导入多个
# from dic_2_file import *              导入了所有，会存在重复定义，最不被建议
# 第1、第2种方式最好，最被推荐




# 3. __name__属性的特性？
# print(__name__) #__name__   如果是本文件话，返回__main__
# print(jl.__name__)#__name__   如果是调用的话，返回文件名称





# 4、什么是全局变量？ 什么是局部变量？
# 具体来说，全局变量和局部变量的区别如下：
# 1. 作用域不同：全局变量的作用域为整个程序，而局部变量的作用域为当前函数或循环等
# 2. 内存存储方式不同：全局变量存储在全局数据区中，局部变量存储在栈区
# 3. 生命期不同：全局变量的生命期和主程序一样，随程序的销毁而销毁，局部变量在函数内部或循环内部，随函数的退出或循环退出就不存在了
# 4. 使用方式不同：全局变量在声明后程序的各个部分都可以用到，但是局部变量只能在局部使用。函数内部会优先使用局部变量再使用全局变量





# 5、函数内部如何修改全局变量？
# global先声明要使用该变量，随后就能修改该全局变量了





# 6、新建一个包pack，在包中新建两个模块module1，module2,   在module1中定义一个函数（函数实现上一次石头、剪刀布游戏的功能），该函数可以通过传入的参数来控制游戏次数，然后在module2中导入module1中定义的函数，并调用。
# 包导入，包：带有__init__.py文件的文件夹
# 导入包，不可以使用import func/ import func as f  来导。。。
# 推荐：
# from pack import filename.func
# from pack import file as f            f.func()
from package_001 import Module2 as m2


if __name__ == '__main__':
    times = int(input("请输入您想玩的次数："))
    m2.package_practise(times)

# 7、请将控制流程 和函数部分学习的内容，画成思维导图提交
# 附件xmind脑图
