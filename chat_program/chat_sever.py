import socket
import threading
import time

sever = socket.socket()
# port = ('localhost',5555)
sever.bind(('localhost',5555))
sever.listen(10)

def handle_conn(conn):
    conn_stat = True
    while conn_stat:
        data = conn.recv(1024)
        if data:
            conn_stat = True
            print("recv:",data.decode('utf-8'))
            conn.send(('%s:%s' % (time.asctime(), data.decode('utf-8'))).encode("utf-8"))
        else:
            print("远程主机断开连接！")
            conn_stat = False

while True:
    socket,addr = sever.accept()
    print("new come:",addr)
    conn = socket
    t = threading.Thread(target = handle_conn,args = (conn,))
    t.start()

