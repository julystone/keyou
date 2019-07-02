import requests
from requests.sessions import Session
from lxml import etree

data = {"userid": "july", "password": "wscxz712718"}

mysession = Session()

res0 = mysession.get(url='http://118.25.173.30:9000/login/', params=data, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'})

res = mysession.get(url='http://118.25.173.30:9000/feedback/', headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'})
# res = requests.get(url='http://118.25.173.30:9000/feedback/')
# res = requests.get(url='https://maoyan.com/board')

html = res.text

print(html)
html = etree.HTML(html)
#
# body = html.xpath('//html/body')
#
datas = html.xpath('//html/body//div[@class="container"]//tbody/*')
#
for item in datas:
    print(item.xpath('.//tr/td[5]/text()'))
#
# #
# 前一位：
# ../div[@="class"]/preceding-sibling::div[1]
# 后一位：
# ../div[@="class"]/following-sibling::div[1]
