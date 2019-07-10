import requests
from requests.sessions import Session
from lxml import etree

data = {"userid": "july", "password": "wscxz712718"}

mysession = Session()

mysession.post(url='http://118.25.173.30:9000/login/', data=data)

res = requests.get(url='https://www.baidu.com/s?wd=xpath', headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'})
# res = requests.get(url='http://118.25.173.30:9000/feedback/')
# res = requests.get(url='https://maoyan.com/board')

html = res.text

html = etree.HTML(html)

body = html.xpath('//html/body')

datas = html.xpath('//html/body//div[@id="content_right"]//div[@class="cr-content "]//tbody/*')

for item in datas:
    print(item.xpath('.//span/a/text()'))

#
# 前一位：
# ../div[@="class"]/preceding-sibling::div[1]
# 后一位：
# ../div[@="class"]/following-sibling::div[1]
