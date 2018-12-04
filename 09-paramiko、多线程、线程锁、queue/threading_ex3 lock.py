__author__ = "Alex Li"

import threading
import time

lock = threading.Lock()
num = 0
t_objs = [] #存线程实例

#在python2中需要加锁，这样才能确保执行完之后，num的最终值为50
def run(n):
    """加锁之后，程序变成了串行"""
    lock.acquire()  #先申请一把锁，确定此时只有本线程才能修改这个数据
    global  num
    num +=1
    time.sleep(0.2)
    lock.release()  #释放锁，加锁为了保证同一时间只有一个程序修改这个数据


for i in range(50):
    t = threading.Thread(target=run,args=("t-%s" %i ,))
    t.start()
    t_objs.append(t) #为了不阻塞后面线程的启动，不在这里join，先放到一个列表里

for t in t_objs: #循环线程实例列表，等待所有线程执行完毕
    t.join()

print("----------all threads has finished...",threading.current_thread(),threading.active_count())

print("num:",num)