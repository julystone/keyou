import requests
from requests.sessions import Session
from lxml import etree
import re
from package_301.common.R_r_excel import ReadExcel

my_excel = ReadExcel("result.xlsx", "Sheet1")

url = 'http://118.25.173.30:9000/'

my_session = Session()


def get_csrf():
    res = my_session.get(url + 'login/')
    csrf = re.search("csrftoken=(.*) for", str(res.cookies)).group(1)
    return csrf


data = {"userid": "july", "password": "wscxz712718", "csrfmiddlewaretoken": get_csrf()}

my_session.post(url + 'login/', data=data)
my_excel.open()
with open("./result.log", 'w', encoding='utf-8') as f:
    for inum in range(350, 700):
        url_new = url + f'feedback/item/{inum}'
        res = my_session.get(url + f'feedback/item/{inum}', timeout=5)
        if res.status_code != 200: continue
        html = res.text
        html = etree.HTML(html)

        mobilephone = html.xpath('//html/body//div[@class="modal-body"]/div[1]/div[2]/div[3]/p/text()')
        version = html.xpath('//html/body//div[@class="modal-body"]/div[1]/div[1]/div[3]/p/text()')
        description = html.xpath('//html/body//div[@class="modal-body"]/div[2]/p[2]/text()')
        line = 1
        if '1' in str(mobilephone) and '2.1.4' in str(version):
            mobilephone = re.search("'联系电话：(.*)'", str(mobilephone)).group(1)
            version = re.search("'应用版本：(.*)'", str(version)).group(1)
            description = re.search("'(.*)'", str(description)).group(1)
            print(url_new, mobilephone, version, description)
            f.write(f"{url_new}\t{mobilephone}\t{version}\t{description}\n")
            my_excel.w_data_origin(line, 1, inum)
            my_excel.w_data_origin(line, 2, url_new)
            my_excel.w_data_origin(line, 3, mobilephone)
            my_excel.w_data_origin(line, 4, version)
            my_excel.w_data_origin(line, 5, description)

            line += 1

my_session.close()
my_excel.close()


# #
# 前一位：
# ../div[@="class"]/preceding-sibling::div[1]
# 后一位：
# ../div[@="class"]/following-sibling::div[1]
