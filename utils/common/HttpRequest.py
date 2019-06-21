# encoding:utf8

# -----------------------------
# @File   :   HttpRequest.py
# @Author :   July401
# @Date   :   2019/6/21
# @Email  :   july401@qq.com
# -----------------------------

import requests


class HttpRequest:
    @classmethod
    def http_request(cls, url, data, method='post'):
        if method.upper() == 'GET':
            res = requests.get(url, data)
        else:  # 执行的是post请求
            res = requests.post(url, data)
        return res.json()  # 解析结果
