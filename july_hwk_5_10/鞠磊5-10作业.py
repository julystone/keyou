import os
import shutil

class hmwk_5_10():

# 1.写入一段文字到TXT中，相对头部偏移5个位置，读取出偏移后的文字。
    def first_ans(self):
        with open('hmwk_5_10_zy1.txt', 'w+', encoding = 'utf-8') as f:
            f.write('1234567890')
            print(f.tell())
            print(f.seek(5))
            print(f.read(5))

# 2.txt里面存了很多数据，都是用逗号隔开的，一个逗号隔开的就是一个数据，一个数据对应列表里面的一个元素。怎么样才能把这些数据读取到出来并且存到list中。
    def second_ans(self):
        list2 = []
        with open('hmwk_5_10_zy2.txt', 'w+', encoding = 'utf-8') as f:
            f.write('1,2,3,4,5,6,7,8,9,0')
            f.seek(0)
            temp = f.readline()
            for i in temp:
                if i==',':
                    continue
                list2.append(i)
        print(list2)
        
        
# 3.txt中存了很多数据，一行为一个请求数据，怎么样才能把这些数据读取到并且存到list中。
# url:http://119.23.241.154:8080/futureloan/mvc/api/member/login,mobilephone:13760246701,pwd:123456
# url:http://119.23.241.154:8080/futureloan/mvc/api/member/login,mobilephone:15678934551,pwd:234555
# url:http://119.23.241.154:8080/futureloan/mvc/api/member/login,mobilephone:15678934551,pwd:234555
# url:http://119.23.241.154:8080/futureloan/mvc/api/member/login,mobilephone:15678934551,pwd:234555
# url:http://119.23.241.154:8080/futureloan/mvc/api/member/login,mobilephone:15678934551,pwd:234555
# 请将文件中的数据读取出来，
# 备注说明：读取出来的 数据保存格式   [{'url':'....','mobilephone':'...','pwd':...'},{.........} ,{.............}]
    def third_ans(self):
    # 先构造下文件
        file_content = '''
url:http://119.23.241.154:8080/futureloan/mvc/api/member/login,mobilephone:13760246701,pwd:123
url:http://119.23.241.154:8080/futureloan/mvc/api/member/login,mobilephone:15678934551,pwd:456
url:http://119.23.241.154:8080/futureloan/mvc/api/member/login,mobilephone:15678934551,pwd:789
url:http://119.23.241.154:8080/futureloan/mvc/api/member/login,mobilephone:15678934551,pwd:112233
url:http://119.23.241.154:8080/futureloan/mvc/api/member/login,mobilephone:15678934551,pwd:445566
'''
        f = open('hmwk_5_10_zy3.txt', 'w')
        f.write(file_content)
        f.close()
        list3 = []
        with open('hmwk_5_10_zy3.txt', 'r') as fp:
            temp = fp.readlines()
            # print(temp)
            for i in temp:
                if 'url' not in i:
                    continue
                else:
                    dic3 = {}
                    dic3['url'] = i.split('url:')[1].split(',')[0]
                    dic3['mobilephone'] = i.split(':')[4].split(',')[0]
                    dic3['pwd'] = i.split(':')[5].strip('\n')
                    list3.append(dic3)
            print(list3)


# 扩展题：不要求提交

# 1、将之前的图书管理系统的数据储存到文件中，账号密码储存到users.txt 图书信息储存到 books.txt中 提示：运行的时候将数据读取出来，退出程序的时候将文件写入到文件中 
    # 图书管理系统代码实现：
    def checkIfNumOccpd(self, is_in, book_No, book_all):
# 检查图书ID是否已被占用
# is_in --"Y"     该书已存在
#       --"N"     该书不存在
# return--1:true
#       --0:false
        flag = 0
        book_all_keys = []
        book_all_keys.extend([i[0] for i in book_all])
        if is_in == "Y":
            if book_No in book_all_keys:
                flag = 1
        elif is_in == "N":
            if book_No not in book_all_keys:
                flag = 1
        return flag

    def checkIfPosOccpd(self, is_occpd, book_Pos, book_all):
# 检查书架位置是否已被占用
# is_occpd--"Y"     位置已被占
#         --"N"     位置尚未空
# return--1:true
#       --0:false
        flag = 0
        book_all_pos = []
        book_all_pos.extend([i[2] for i in book_all])
        if is_occpd == "Y":
            if book_Pos in book_all_pos:
            #如果位置已有书
                flag = 1
        elif is_occpd == "N":
            if book_Pos not in book_all_pos:
            #如果位置已有书
                flag = 1
        return flag

    def print_menu(self):
        if input("\n\n回车清屏，任意键取消") == '':
            os.system("cls")
        idx = ["", "【1】:添加图书", "【2】:修改图书", "【3】:删除图书", "【4】:查询图书", "【5】:退出程序", ""]
        for items in idx:
            print("%s"%items.center(32-len(items), '-'))

    def register(self, account_info):
        print("#注册界面")
        username = input("请输入账号：")
        account_all = []
        for i in account_info:
            account_all.append(i[0])
        while username in account_all:
            print("账号已存在，请检查并重新输入")
            if input("\n\n回车重新输入，任意键返回上一菜单") == '':
                username = input("请重新输入账号：")
            else:
                return
        password = input("请输入密码：")
        print("账号注册成功，请返回并重新登录")
        account_info.append([username, password])
        # 账号写入account_info.txt文件中

    def login(self, account_info):
        print("#登陆界面")
        username = input("请输入账号：")
        password = input("请输入密码：")
        account_all = []
        for i in account_info:
            account_all.append(i[0])
        if username not in account_all:
            print("账号不存在，请检查并重新输入")
        elif password != account_info[account_all.index(username)][1]:
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
        book = [book_No, book_Name, book_Pos]
        book_all.append(book)
        # print(book_all)
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
        for i in book_all:
            if i[0] == book_No:
                book_No_operated = book_all.index(i)
        book = [book_No, book_Name, book_Pos]
        book_all[book_No_operated] = book
        print("********【系统】图书修改成功")

    def del_book(self, book_all):
        print("#删除图书")
        book_No = input("请输入图书编号：")
        while self.checkIfNumOccpd("N", book_No, book_all):
        #如果编号不存在，则报错
            print("********【Err】不存在该图书，无法删除")
            if input("\n\n回车重新输入，任意键返回上一菜单") == '':
                book_No = input("请重新输入图书编号：")
            else:
                return
        for i in book_all:
            if i[0] == book_No:
                book_No_operated = book_all.index(i)
        book_all.pop(book_No_operated)
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
                    book_No = input("请重新输入图书编号：")
                else:
                    return
            for i in book_all:
                if i[0] == book_No:
                    book_No_operated = book_all.index(i)
            print("\n********【系统】该书信息如下：\n********【系统】图书名称：《{0}》\n********【系统】图书位置：{1}".format(book_all[book_No_operated][1],book_all[book_No_operated][2]))
        elif search_me =='2' or search_me =='':
        #返回所有书籍
            print("\n********【系统】所有书信息如下：\n********【系统】图书编号\t图书名称\t图书位置")
            for key_inter in book_all:
                print("********【系统】No.{}\t\t《{}》\t\t{}".format(key_inter[0], key_inter[1] ,key_inter[2]))
        else:
            print("********【Err】输入错误")

    def account_init(self, account_info):
        with open('account_info.txt', 'a+', encoding='utf-8') as f_account_info:
            f_account_info.seek(0)
            account_info_lines = f_account_info.readlines()
            for i in account_info_lines:
                if i == '\n':
                    continue
                else:
                    list = []
                    list.append(i.split("\'")[1])
                    list.append(i.split("\'")[3])
                    account_info.append(list)

    def bookshell_init(self, book_all):
        with open('book_info.txt', 'a+', encoding='utf-8') as f_book_info:
            f_book_info.seek(0)
            book_info_lines = f_book_info.readlines()
            for i in book_info_lines:
                if i == '\n':
                    continue
                else:
                    list = []
                    list.append(i.split("\'")[1])
                    list.append(i.split("\'")[3])
                    list.append(i.split("\'")[5])
                    book_all.append(list)

    def library_main(self):
        account_info = []
        self.account_init(account_info)
        book_all = []
        self.bookshell_init(book_all)
        while 1:
            sel = input("\n\n是否需要注册新账号？(Y/N)\n")
            if sel =='Y' or sel == 'y':
                self.register(account_info)
            elif sel == 'N' or sel == 'n':
                print("用户选择不注册账户，正在为您跳转\n")
            else:
                print("用户输入错误\n")
                continue
            if self.login(account_info):
                while(1):
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
                # 账号信息写入account_info.txt文件中
                with open('account_info.txt', 'w', encoding='utf-8') as f:
                    for i in account_info:
                        f.write("\n'{}','{}'".format(i[0], i[1]))
                # 书籍信息写入book_info.txt文件中
                with open('book_info.txt', 'w', encoding='utf-8') as f:
                    for i in book_all:
                        f.write("\n'{}','{}','{}'".format(i[0], i[1], i[2]))
                break


# 2、实现一个文件复制器文件copy器,传入一个文件夹的路径，会自动将该路径下所有的文件复制到 当前路径下，一个名为 '原文件夹名+副本‘ 的文件夹下面
# 参考案例：文件批量改名案例
    def folder_copy(self, dir_path):
        file_list = os.listdir(dir_path)
        backupdir = dir_path + r'\backup'
        if not os.path.isdir(backupdir):
            os.mkdir(backupdir)
        os.chdir(backupdir)
        print(file_list)
        for name in file_list:
            if os.path.isfile(os.path.join(dir_path, name)):
                new_name = name + '_副本'
                shutil.copy(os.path.join(dir_path, name), os.path.join(backupdir, new_name))


if __name__ == "__main__":
    home = hmwk_5_10()
    home.first_ans()

    print("-------------------------------------")
    home.second_ans()

    print("-------------------------------------")
    home.third_ans()

    print("-------------------------------------")
    home.library_main()

    print("-------------------------------------")
    home.folder_copy(r"C:\Users\esunny\Documents\practice")