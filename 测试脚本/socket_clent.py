import socket

clent = socket.socket()
clent.connect(('localhost',5555))
while True:
    data  = input(">>:")
    if len(data) == 0: continue
    clent.send(data.encode("utf-8"))
    data_recv = clent.recv(1024)
    print("recv:",data_recv.decode("utf-8"))