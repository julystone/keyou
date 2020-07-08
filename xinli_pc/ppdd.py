# -*- coding: utf-8 -*-
# @File   :   ppdd.py
# @Author :   julystone
# @Date   :   2020/5/22 9:38
# @Email  :   july401@qq.com


import pandas as pd
import pymysql

mysql_cn = pymysql.connect(host='111.231.17.167', port=3306, user='root', passwd='Esunny123456!', db='CspNewsMgr')
df = pd.read_sql('select * from TCommodityF10;', con=mysql_cn)
df = df.replace(r"\n", "", regex=True)
df = df.replace(r"\r\r", "", regex=True)

print(df["FTradingTime"])

df.to_csv("./F10", index=0, sep=",", quoting=1)
