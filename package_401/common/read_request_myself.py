# -*-coding:utf-8-*-
"""
==========================
author:HuaHua
time:2019-7-2
E-mail:61283133@qq.com
==========================
"""
from package_401.common.client import client
import suds
import json

"""
webservice接口
"""
url = "http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl"

# 获取该地址下的webservice对象
web_service = client.Client(url=url)
print(web_service)

# 构造请求参数
data = {"client_ip": 00, "tmpl_id": 1, "mobile": 13358341234}

# 发送请求

res = web_service.service.sendMCode(data)

print(dict(res))
#

# sql = "SELECT * FROM  sms_db_{}.t_mvcode_info_{}".format(data['mobile'][-2:],data['mobile'][-3])
#
# print(sql)
