import json

import itchat

itchat.auto_login()
data = itchat.get_friends()
in_json = json.dumps(data, indent=10)
# print(in_json)

out_json = json.loads(in_json, encoding='utf-8')
for i in out_json:
    i2print = i['RemarkName'] if i['RemarkName'] != '' else i['NickName']
    print('{}\'s signature is :{}'.format(i2print, i['Signature']))
