# encoding:utf8
# @File   :   generate.py
# @Author :   July401
# @Date   :   2019/6/11
# @Email  :   july401@qq.com

import pandas as pd


class Case:
    pass


class ReadExcelPd:
    """
    封装一个读取用例的excel类
    # 实现读取用例数据
    # 实现写入数据的功能
    """

    def __init__(self, file_name, sheet_name):
        self.dp = pd.read_excel(file_name, sheet_name=sheet_name)
        self.filename = file_name
        self.sheetname = sheet_name
        self.max_row = self.dp.shape[0]
        self.max_column = self.dp.shape[1]

    def __del__(self):
        pass

    def read_data_obj(self):
        result = self.dp.to_dict(orient='records')
        case_all_list = []
        for i in result:
            case_one = Case()
            for items in i.items():
                if items[1] != items[1]:
                    continue
                setattr(case_one, items[0], items[1])
            case_all_list.append(case_one)
        return case_all_list

    def w_data(self, row, column, data):
        self.dp.iloc[row - 1, column - 1] = data

    def w_save(self):
        self.dp.to_excel(self.filename[:-5] + f'{self.sheetname}.xlsx', self.sheetname)

    def r_max(self):
        return self.max_row, self.max_column


if __name__ == '__main__':
    r = ReadExcelPd('api_test.xlsx', 'withdraw')
    r.w_data(1, 2, 3)
    r.w_save()
    print(r.r_max()[0])
