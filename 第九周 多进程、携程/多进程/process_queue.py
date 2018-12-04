from multiprocessing import Process,Queue
import os

def f(qq):
    qq.put(["Hello BlingBling!",os.getpid()])

if __name__ =="__main__":
    q = Queue()       #这是进程通信的Q
    p = Process(target=f,args=(q,))
    p.start()
    print(os.getpid(),q.get())
