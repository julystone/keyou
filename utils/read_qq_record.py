import re

from package_401.common.R_r_excel import ReadExcel

SIGN_PAT = r"打卡(\d*)次(.*)"
NICK_PAT = r"(落花.*(?=\())"
DATE_PAT = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})"

EXCEL_PATH = "./ALL.xlsx"
TXT_PATH = "./『联盟群』花落闪暖，国服安一.txt"

with open(TXT_PATH, 'r', encoding='utf-8') as f:
    txt_file = f.readlines()


def check_if_info(string):
    if re.search(DATE_PAT, string) is None:
        return None
    return re.search(DATE_PAT, string).group(1), re.search(DATE_PAT, string).group(2)


def inter_trans(inter):
    inter = inter.lower()
    inter = inter.strip("分")
    special_symbol = ["w", "万"]
    for symbol in special_symbol:
        if symbol in inter:
            raw_int = inter.split(symbol)[0]
            if "." in raw_int:
                return float(raw_int) * 10000
            raw_float = inter.split(symbol)[1]
            return float(raw_int + "." + raw_float) * 10000
        else:
            return float(inter)


def table_init():
    fo = ReadExcel(EXCEL_PATH, "Sheet1")
    fo.clear_sheet()
    column = 1
    titles = ("日期", "时间", "昵称", "单次挑战分数", "总次数", "总分", "部分未解析数据")
    widths = ("14", "14", "24", "14", "14", "14", "24")
    for (title, width) in zip(titles, widths):
        fo.w_data(1, column, title)
        fo.set_column_width(chr(ord("A") + column - 1), width)
        fo.set_font(1, column)
        column += 1
    return fo


if __name__ == '__main__':
    file = table_init()

    flag = 0  # 判断是否为需要记录的文本
    line_no = 2  # 数据记录从第2行开始
    for content in txt_file[::-1]:
        if flag:
            temp = check_if_info(content)
            if temp is None:
                continue
            flag = 0
            (date, time) = temp
            nickname = re.search(NICK_PAT, content).group(0)
            file.w_data(line_no, 1, date)
            file.w_data(line_no, 2, time)
            file.w_data(line_no, 3, nickname)
            line_no += 1
        try:
            if "单次4万六" in content:
                print(111)
            times = re.search(SIGN_PAT, content).group(1)
            average = re.search(SIGN_PAT, content).group(2)
            flag = 1
            total = int(times) * inter_trans(average)
            file.w_data(line_no, 4, average)
            file.w_data(line_no, 5, times)
            file.w_data(line_no, 6, total)
        except AttributeError:
            pass
        except ValueError:
            file.w_data(line_no, 7, content)
