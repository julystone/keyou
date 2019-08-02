import re


class Context:
    admin_user = "july"
    admin_pwd = "123456"

    def replace_new(self, be_replaced):
        zhengze = "\$\{(.*?)}"
        while re.search(zhengze, be_replaced):
            match = re.search(zhengze, be_replaced)
            print('match:', match)
            key2 = match.group(1)  # 查到一个就替换
            print('key2:', key2)
            if hasattr(Context, key2):
                value = getattr(Context, key2)
                print('value:', value)
                be_replaced = re.sub(zhengze, value, be_replaced, count=1)
            else:
                return None
        return be_replaced


if __name__ == '__main__':
    ss = '{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'
    a = Context()
    print(a.replace_new(ss))
