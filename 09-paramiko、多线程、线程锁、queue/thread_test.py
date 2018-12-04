import threading
import time
def add(n):
    global num
    time.sleep(0.2)
    num = num + 1
    print("result-%s-%s"%(n,num))
    return num
num = 1
for i in range(10):
    t = threading.Thread(target=add,args=(i,))
    t.start()
time.sleep(1)
print("finally",num+1)