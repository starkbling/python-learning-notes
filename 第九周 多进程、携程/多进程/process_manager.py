from multiprocessing import Process,Manager
import os

def fm(d,l):
    d[os.getpid()] = 'BlingBling'
    l.append(os.getpid())

if __name__ == '__main__':         #这段代码主要是确定运行的是主进程
    p_list = []
    with Manager() as manager:
        d = manager.dict()    #指定字典变量
        l = manager.list(range(5))   #指定列表变量
        for i in range(5):
            p = Process(target=fm,args=(d,l))
            p.start()
            p1= Process()
            p_list.append(p)
        for pc in p_list:
            pc.join()
        print(d)
        print(l)