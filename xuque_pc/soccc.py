import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET:指定可以在不同电脑之间通信
# socket.SOCK_STREAM:指定创建TCP套接字
address = ('www.baidu.com', 80)
s.connect(address)


# http请求，要加请求头
http_header = b'''GET / HTTP/1.1\r
Host: www.epolestar.zentaopm.com\r
Connection: keep-alive\r
\r
'''

http_header = b'''GET / HTTP/1.1\r
Host: www.baidu.com\r
Connection: keep-alive\r
\r
'''

s.send(http_header)
str_content = ""

while True:
    content = s.recv(2048)
    str_content += content.decode('utf-8')
    # print(content)
    if not content: break

print(str_content)

s.close()