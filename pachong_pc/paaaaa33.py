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
line = 2
with open("./result.log", 'w', encoding='utf-8') as f:
    for feedback_id in range(350, 700):
        url_new = url + f'feedback/item/{feedback_id}'
        res = my_session.get(url + f'feedback/item/{feedback_id}', timeout=5)
        if res.status_code != 200: continue
        html = res.text
        html = etree.HTML(html)

        hardVersion = html.xpath('//html/body//div[@class="modal-body"]/div[1]/div[1]/div[1]/p/text()')
        Android = html.xpath('//html/body//div[@class="modal-body"]/div[1]/div[1]/div[2]/p/text()')
        AppVersion = html.xpath('//html/body//div[@class="modal-body"]/div[1]/div[1]/div[3]/p/text()')

        DeviceFac = html.xpath('//html/body//div[@class="modal-body"]/div[1]/div[2]/div[1]/p/text()')
        MobilePhone = html.xpath('//html/body//div[@class="modal-body"]/div[1]/div[2]/div[3]/p/text()')
        Desc = html.xpath('//html/body//div[@class="modal-body"]/div[2]/p[2]/text()')

        if not html.xpath('//html/body//div[@class="modal-body"]/div[3]'):
            picExist = False
        else:
            picExist = True

        or_list = [hardVersion, Android, AppVersion, DeviceFac, MobilePhone, Desc]
        if '1' in str(MobilePhone) and '2.1.4' in str(AppVersion):
            or_list = [hardVersion, Android, AppVersion, DeviceFac, MobilePhone, Desc]
            op_list = []
            for item in or_list:
                try:
                    op_list.append(re.search("：(.*)'", str(item)).group(1))
                except AttributeError:
                    op_list.append(re.search("'(.*)'", str(item)).group(1))
            hardVersion, Android, AppVersion, DeviceFac, MobilePhone, Desc = op_list

            f.write(f"{url_new}\t{MobilePhone}\t{AppVersion}\t{Desc}\n")
            my_excel.w_data_origin(line, 1, feedback_id)
            my_excel.w_data_origin(line, 2, hardVersion)
            my_excel.w_data_origin(line, 3, DeviceFac)
            my_excel.w_data_origin(line, 4, Android)
            my_excel.w_data_origin(line, 5, AppVersion)
            my_excel.w_data_origin(line, 6, url_new)
            my_excel.w_data_origin(line, 7, MobilePhone)
            my_excel.w_data_origin(line, 8, picExist)
            my_excel.w_data_origin(line, 9, Desc)

            line += 1

my_session.close()
my_excel.close()
my_excel.save()

# #
# 前一位：
# ../div[@="class"]/preceding-sibling::div[1]
# 后一位：
# ../div[@="class"]/following-sibling::div[1]
