# -*- coding:utf-8 -*-
__Author__ = 'BLINGBLING'

import select
import queue
import socket

sever = socket.socket()
sever.bind(("localhost",5500))
sever.listen(1000)
sever.setblocking(False)

inputs =[sever,]
outputs = []
write_dic  = {}
while True:
    readable, writeable, exceptional = select.select(inputs,outputs,inputs)
    for r in readable:
        if r is sever:
            conn,addr = sever.accept()
            print("新连接:",addr)
            inputs.append(conn)
            write_dic[conn] = queue.Queue()  # 初始化一个队列，后面存要返回给这个客户端的数据
        else:
            try:
                data = r.recv(1024)
                if data:
                    print("recv:",data)
                    write_dic[r].put(data)
                    outputs.append(r)
            except (ConnectionResetError,ConnectionAbortedError):
                print("客户端已断开链接！",r)
                if r in outputs:
                    outputs.remove(r)
                del write_dic[r]
                inputs.remove(r)

    for w in writeable:
        data_sendback = write_dic[w].get()
        w.send(data_sendback)
        print("send:",data_sendback)
        outputs.remove(w)

    for e in exceptional:
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)
        del write_dic[e]  #删除异常列表中的链接