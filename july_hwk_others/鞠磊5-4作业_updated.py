import os


class Homework:

    # 8、将上次作业的图书管理系统改成函数版本，每个功能封装成一个函数，原来功能上扩展，启动程序首先提示功能选项：
    # 【1】登录，【2】注册，完成注册功能
    # main()：控制整个程序的运行流程
    # print_menu():打印菜单
    # login(): 登录功能                                             register：注册功能
    # add_book():添加图书                                      del_book():删除图书
    # all_book():显示所有图书                                  find_book: 查找图书
    # update_book():修改图书
    # 修复bug（扩展，不要求提交到作业）：
    # 添加图书时，图书的id不能重复，图书名可以重复；

    # 删除查询修改的时候，输入图书名之后提供所有同名的图书，给用户选择，用户可以选择其中的一本进行操作。
    @classmethod
    def checkIfNumOccpd(cls, is_in, book_No, book_all):
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

    @classmethod
    def checkIfPosOccpd(cls, is_occpd, book_Pos, book_all):
        # 检查书架位置是否已被占用
        # is_occpd--"Y"     位置已被占
        #         --"N"     位置尚未空
        # return--1:true
        #       --0:false
        flag = 0
        if is_occpd == "Y":
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

    @classmethod
    def print_menu(cls):
        if input("\n\n回车清屏，任意键取消") == '':
            os.system("cls")
        print("")
        idx = ["", "【1】:添加图书", "【2】:修改图书", "【3】:删除图书", "【4】:查询图书", "【5】:退出程序", ""]
        # #         print("""
# ********************************
# ********【1】:添加图书
# ********【2】:修改图书
# ********【3】:删除图书
# ********【4】:查询图书
# ********【5】:退出
# ********************************
# """)
        for items in idx:
            print("%s"%items.center(32-len(items), '-'))
        # print("".center(32,'*'))
        # print("【1】:添加图书".center(32,'*'))
        # print("【2】:修改图书".center(32,'*'))
        # print("【3】:删除图书".center(32,'*'))
        # print("【4】:查询图书".center(32,'*'))
        # print("【5】:退出".center(32,'*'))

    def register(self, account_info):
        print("#注册界面")
        username = input("请输入账号：")
        while username in account_info.keys():
            print("账号已存在，请检查并重新输入")
            if input("\n\n回车重新输入，任意键返回上一菜单") == '':
                username = input("请重新输入图书编号：")
            else:
                return
        password = input("请输入密码：")
        print("账号注册成功，请返回并重新登录")
        account_info[username] = password

    def login(self, account_info):
        print("#登陆界面")
        username = input("请输入账号：")
        password = input("请输入密码：")
        if username not in account_info.keys():
            print("账号不存在，请检查并重新输入")
        elif password != account_info.get(username):
            print("密码错误，请检查并重新输入")
        else:
            print("账号密码正确，登录成功")
            print("------欢迎进入图书管理系统------")
            return True
        return False

    def add_book(self, book_all):
        print("#添加图书")
        book_No = input("请输入图书编号：")
        while self.checkIfNumOccpd("Y", book_No, book_all):
        #如果编号已被占据，则报冲突
            print("********【Err】图书编号冲突，添加失败")
            if input("\n\n回车重新输入，任意键返回上一菜单") == '':
                book_No = input("请重新输入图书编号：")
            else:
                return
        book_Name = input("请输入图书名称：")
        book_Pos = input("请输入图书位置：")
        while self.checkIfPosOccpd("Y", book_Pos, book_all):
        #如果位置已被占据，则报冲突
            print("********【Err】该位置已被占据，添加失败")
            if input("\n\n回车重新输入，任意键返回上一菜单") == '':
                book_Pos = input("请重新输入图书位置：")
            else:
                return
        book = {'book_Name':book_Name,'book_Pos':book_Pos}
        book_all[book_No]=book
        print("********【系统】图书添加成功")

    def update_book(self, book_all):
        print("#修改图书")
        book_No = input("请输入图书编号：")
        while self.checkIfNumOccpd("N", book_No, book_all):
        # 如果编号不存在，则报错
            print("********【Err】不存在该图书，无法修改")
            if input("\n\n回车重新输入，任意键返回上一菜单") == '':
                book_No = input("请重新输入图书编号：")
            else:
                return
        book_Name = input("请输入更改后的图书名称：")
        book_Pos = input("请输入更改后的图书位置：")
        while self.checkIfPosOccpd("Y", book_Pos, book_all):
        # 如果位置已被占据，则报冲突
            print("********【Err】该位置已被占据，修改失败")
            if input("\n\n回车重新输入，任意键返回上一菜单") == '':
                book_Pos = input("请重新输入图书位置：")
            else:
                return
        book = {'book_Name':book_Name,'book_Pos':book_Pos}
        book_all[book_No]=book
        print("********【系统】图书修改成功")

    def del_book(self, book_all):
        print("#删除图书")
        book_No = input("请输入图书编号：")
        while self.checkIfNumOccpd("N", book_No, book_all):
        #如果编号不存在，则报错
            print("********【Err】不存在该图书，无法删除")
            if input("\n\n回车重新输入，任意键返回上一菜单") == '':
                book_Pos = input("请重新输入图书位置：")
            else:
                return
        del book_all[book_No]
        print("********【系统】图书删除成功")

    def find_book(self, book_all):
        print("#查询图书")
        search_me = input("\n\n查询单本【1】，查询全部【2】，默认为全部")
        if search_me == '1':
            book_No = input("请输入图书编号：")
            while self.checkIfNumOccpd("N", book_No, book_all):
            #如果编号不存在，则报错
                print("********【Err】不存在该图书")
                if input("\n\n回车重新输入，任意键返回上一菜单") == '':
                    book_Pos = input("请重新输入图书位置：")
                else:
                    return
            print("\n********【系统】该书信息如下：\n********【系统】图书名称：《{0}》\n********【系统】图书位置：{1}".format(book_all[book_No]["book_Name"],book_all[book_No]["book_Pos"]))
        elif search_me =='2' or search_me =='':
        #返回所有书籍
            print("\n********【系统】所有书信息如下：\n********【系统】图书编号\t图书名称\t图书位置")
            for key_inter in book_all.keys():
                print("********【系统】No.{}\t\t《{}》\t\t{}".format(key_inter, book_all[key_inter]["book_Name"],book_all[key_inter]["book_Pos"]))
        else:
            print("********【Err】输入错误")

    def fifth_ans(self):
        account_info = {'july': '111111', 'lemon': '222222'}
        book_all = {}
        while 1:
            sel = input("\n\n是否需要注册新账号？(Y/N)\n")
            if sel == 'Y' or sel == 'y':
                self.register(account_info)
            elif sel == 'N' or sel == 'n':
                print("用户选择不注册账户，正在为您跳转\n")
            else:
                print("用户输入错误\n")
                continue
            if self.login(account_info):
                while 1:
                    self.print_menu()
                    num = input("请输入您的选项：")
                    if num == '1':
                        self.add_book(book_all)
                    elif num == '2':
                        self.update_book(book_all)
                    elif num == '3':
                        self.del_book(book_all)
                    elif num == '4':
                        self.find_book(book_all)
                    elif num == '5':
                        print("#退出")
                        break
                    else:
                        print("输入错误")
                break

if __name__ == "__main__":
    home = Homework()
    home.fifth_ans()


