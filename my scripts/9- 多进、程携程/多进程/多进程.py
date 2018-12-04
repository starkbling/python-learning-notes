from multiprocessing import Process
import time,threading
import os

def tt():
    print(threading.get_ident())  #获取线程的id
    pass

def run(name):
    time.sleep(2)
    print('hello %s'%name)
    t = threading.Thread(target=tt,)
    t.start()

if __name__ == '__main__':
    for i in range(20):
        p = Process(target=run, args = ("bling %s"%i,))
        p.start()
        # p.join()