import requests
from lxml import etree

res = requests.get(url='https://www.baidu.com/s?wd=xpath')
# res = requests.get(url='https://maoyan.com/board')

html = res.text

html = etree.HTML(html)

head = html.xpath('//html/body')

datas = html.xpath('//div[@id="content_right"]//div[@class="cr-content"]')

for item in datas:
    print(item.xpath('.//span[@class="c-index c-index-hot1 c-gap-icon-right-small"]/a/text()'))

#
# 前一位：
# ../div[@="class"]/preceding-sibling::div[1]
# 后一位：
# ../div[@="class"]/following-sibling::div[1]
