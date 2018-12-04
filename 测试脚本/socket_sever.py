import socket
import threading
import time

def handle_conn(conn,addr):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                print("远程主机断开连接！")
                break
            print("recv:",data.decode('utf-8'))
            conn.send(('%s:%s' % (time.asctime(), data.decode('utf-8'))).encode("utf-8"))
        except Exception as  e:
            print('addr:%s error:%s'%(addr,e))
            break

sever = socket.socket()
# port = ('localhost',5555)
sever.bind(('localhost',5555))
sever.listen(10)
conn_list = []

print("waiting for connecting ...")
while True:
    socket,address = sever.accept()
    print("new come:",address)
    conn = socket
    addr = address
    t = threading.Thread(target = handle_conn,args = (conn,addr))
    t.start()
    conn_list.append(conn)