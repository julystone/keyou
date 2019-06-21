# @File   :   mysql_pc.py
# @Author :   July401
# @Date   :   2019/6/4
# @Email  :   july401@qq.com

import pymysql

con = pymysql.connect(host='localhost',
                      port=3306,
                      database='test',
                      user='root',
                      password='mysql'
                      )

cur = con.cursor()
# 增加
sql = 'Insert into students Value(0, "musen", 55, 176.0, 1, 5, 0)'
# 删除

# 查找   查询操作，不用提交（未有修改操作）
sql = 'Select * from students Where name = "musen"'
res = cur.execute(sql)
data1 = cur.fetchone()
data_all = cur.fetchall()
data_part = cur.fetchmany(size=2)
print(data1)

# 修改
sql = 'Update students Set name = "july" Where name = "musen"'
res = cur.execute(sql)  # res是影响的行数
print(res)

# python中操作mysql数据库，默认开启事务。。。事务开启了，必须要提交才生效
con.commit()

# 关闭游标，断开连接
cur.close()
con.close()
