__author__ = "Alex Li"
#客户端
import socket

client = socket.socket() #声明socket类型，同时生成socket连接对象
client.connect(('localhost',9999))   #指明连接的地址和端口号

while True:
    msg = input(">>:").strip()
    if len(msg) == 0:continue
    client.send(msg.encode("utf-8"))   #发送字节型数据
    data = client.recv(1024)  #接收服务器返回的数据
    print("recv:",data.decode())
client.close()
