# encoding:utf8

# -----------------------------
# @File   :   request_1.py
# @Author :   July401
# @Date   :   2019/6/11
# @Email  :   july401@qq.com
# -----------------------------

import requests

register_url = 'http://test.lemonban.com/futureloan/mvc/api/member/register'
register_params = {"mobilephone": "13912345611", "pwd": "123456"}
# register_res1 = requests.get(url=register_url, params=register_params)
register_res1 = requests.post(url=register_url, data=register_params)
register_res2 = requests.sessions.Session().post(url=register_url, data=register_params)
print(register_res1.text)
print(register_res2.text)

# login_url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
# login_params = {"mobilephone": "13912345611", "pwd": "123456"}
# session = requests.sessions.Session()
# login_res1 = session.post(url=login_url, data=login_params)
# print(login_res1.text)
#
# recharge_url = 'http://test.lemonban.com/futureloan/mvc/api/member/recharge'
# recharge_params = {"mobilephone": "13912345611", "amount": "500"}
# recharge_res1 = session.post(url=recharge_url, data=recharge_params)
# print(recharge_res1.text)
#
# withdraw_url = 'http://test.lemonban.com/futureloan/mvc/api/member/withdraw'
# withdraw_params = {"mobilephone": "13912345611", "amount": "500"}
# withdraw_res1 = session.post(url=withdraw_url, data=withdraw_params)
# print(withdraw_res1.text)
#
# list_url = 'http://test.lemonban.com/futureloan/mvc/api/member/list'
# list_params = {"mobilephone": None, "amount": None}
# list_res1 = session.post(url=list_url, data=list_params)
# print(list_res1.text)
