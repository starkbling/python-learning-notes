__author__ = "Alex Li"

import socket ,os,time,hashlib
server = socket.socket()
server.bind(('localhost',9999) )

server.listen()

while True:
    conn, addr = server.accept()
    print("new conn:",addr)
    while True:
        print("等待新指令")
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
            break
        cmd,filename = data.decode().split()
        print(filename)
        if os.path.isfile():  #判断文件是否存在
            f = open(filename,"rb")
            m = hashlib.md5()   #设置一个md5变量
            filesize = os.stat(filename).st_size
            conn.send(str(file_size).encode())   #发送文件大小
            conn.recv(1024)    #等待客户端确认
            for line in f:
                m.update(line)
                conn.send(line)
            print("file md5:",m.hexdigest())
            f.close

        print("send done")

server.close()

import hashlib
m = hashlib.md5()