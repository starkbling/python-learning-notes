# -*- coding:utf-8 -*-
__Author__ = 'BLINGBLING'

import socket

client = socket.socket()
client.connect(("localhost",5500))
while True:
    data_s = input(">>:")
    if data_s:
        client.send(data_s.encode("utf-8"))
        data_r = client.recv(1024)
        print(data_r.decode("utf-8"))
    else:
        client.close()
        break