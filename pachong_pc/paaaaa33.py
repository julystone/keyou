import requests
from requests.sessions import Session
from lxml import etree

data = {"userid": "july", "password": "wscxz712718"}

my_session = Session()
data = {"userid": "july", "password": "wscxz712718"}

res = my_session.post(url='http://118.25.173.30:9000/login/', headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}, data=data)
# res = requests.get(url='http://118.25.173.30:9000/feedback/')
# res = requests.get(url='https://maoyan.com/board')

html = res.text

print(html)
html = etree.HTML(html)
#
# body = html.xpath('//html/body')
#
datas = html.xpath('//html/body/*')
#
for item in datas:
    print(item)
#
# #
# 前一位：
# ../div[@="class"]/preceding-sibling::div[1]
# 后一位：
# ../div[@="class"]/following-sibling::div[1]
