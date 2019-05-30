from math import floor
from math import ceil
import re
import pandas as pd

def max_min(amount_min, amount_max, e = 1):
    # e为敏感参数 默认为
    # e = -1
    burden = amount_max - amount_min
    temp = burden
    while temp > 1:
        e += 1
        temp /= 40
    amount_max_temp = ceil(amount_max / pow(40, e-1)) * pow(40, e-1)
    amount_min_temp = floor(amount_min / pow(40, e-1)) * pow(40, e-1)
    return amount_min_temp, amount_max_temp


def try_except_else_finally():
    try:
        2/0
    except:
        print("except")
    else:
        print("else")
    finally:
        print("finally")


def exception_practise():
    i = 1
    while i:
        try:
            player_choice_init = input("请输入要出的拳：\n石头【1】  剪刀【2】  布【3】")
            if player_choice_init not in ["1", "2", "3"]:
                raise TypeError
            break
        except (ValueError, TypeError) as Err:
            print('出错了，必须是[1,2,3]区间的\n')

        # i -= 1


def re_ps2():
    str1 = r'everasdqgfeverqasdaaaeeeqqeveracaeeewqaccc'
    regex = r'ever((?!ever).)*ccc'
    res = re.search(regex, str1).group()
    print(res)


def xl_ps():
    pattern = re.compile(r"ever((?!ever).)*ccc")
    str1 = u'everasdqgfeverqasdaaaeeeqqeveracaeeewqaccc'
    print(pattern.search(str1))


def xing_ps(a,b,c):
    print(a,b,c)


def pd_pc():
    res = pd.read_excel('cases.xlsx', 'Sheet1')
    # 读取单列
    print(res.data)
    print(res['data'])
    # 读取多列
    print(res[['case_id', 'data']])
    print(" ".center(64, '-'))

    # 读取单行
    print(res.iloc[0])  # 读取单行，不包括表头，0是第一行
    # 读取多行
    print(res.iloc[[0, 1]])
    print(" ".center(64, '-'))

    # 读取单元格
    print(res.data[2], res['data'][2])         # 比较舒服的定位方式
    print(res.iloc[2][1], res.iloc[2]['data'])
    print(" ".center(64, '-'))

    # iloc 与 loc 的区别
    # iloc 只支持数字索引， loc 只支持文字索引（例子中的1,3  是恰巧）
    # loc 支持bool判断
    print(res.iloc[[1, 3], [1, 3]])
    print(res.loc[[1, 3], ['data', 'expected']])
    print(res.case_id == 0)                     # 返回true 或者 false
    print(res.loc[res.case_id == 0])            # loc出来true的返回

    # pandas 写入操作不够强大，它会重置格式
    # res['result'][0] = 'success'
    # with pd.ExcelWriter('cases_pd.xlsx') as writer:
    #     res.to_excel(writer, index=False)

    # pandas读csv文件
    csvdf = pd.read_csv("data.log")
    csvdf_new = csvdf.loc[csvdf[' Success'] == 0]
    csvdf_new_tt_max = max(csvdf_new[' TestTime'])
    csvdf_new_tt_min = min(csvdf_new[' TestTime'])
    print(csvdf_new[' TestTime'])


if __name__ == '__main__':
    pd_pc()
    pass