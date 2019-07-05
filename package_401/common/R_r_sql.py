# @File   :   R_r_sql.py
# @Author :   July401
# @Date   :   2019/6/15
# @Email  :   july401@qq.com

import pymysql

from package_301.common.R_r_config import my_config

"""
输入sql，返回一条或多条
"""


class Mysql:
    def __init__(self):
        section = 'database'
        host = my_config.get(section, 'host')
        user = my_config.get(section, 'user')
        password = my_config.get(section, 'password')
        database = my_config.get(section, 'database')
        port = my_config.get(section, 'port')
        charset = my_config.get(section, 'charset')
        self.con = pymysql.connect(host=host, user=user, password=password, database=database, port=eval(port),
                                   charset=charset)
        self.cur = self.con.cursor()

    def __del__(self):
        self.cur.close()
        self.con.close()

    def select(self, sql, resultmode=0):
        self.con.commit()
        self.cur.execute(sql)
        self.con.commit()
        if resultmode == 0:
            temp = self.cur.fetchone()
        elif resultmode == 1:
            temp = self.cur.fetchall()
        elif resultmode == 2:
            temp = self.cur.fetchmany(size=4)
        # df = pd.read_sql(sql=sql, con=self.con)
        return temp

    def insert(self, sql):
        self.cur.execute(sql)
        self.con.commit()


my_sql = Mysql()

if __name__ == '__main__':
    sql = f'SELECT leaveamount FROM member where mobilephone = 13912345611'
    res = my_sql.select(sql)
    print(res)
