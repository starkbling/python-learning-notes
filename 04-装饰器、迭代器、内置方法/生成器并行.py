__author__ = "Alex Li"

import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield

       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))

# c = consumer("ChenRonghua")
# c.__next__()
# c.__next__()

# b1= "韭菜馅"
# b2 ="玉米猪肉馅"
# c.__next__()
# c.send(b1)   #send中的值被yield接受了，从而给baozi赋值“韭菜馅”，同时调用了yield，后面的语句继续运行
# c.send(b2)   #send中的值被yield接受了，从而给baozi赋值“玉米猪肉馅”，同时调用了yield，后面的语句继续运行
# c.__next__()

def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("%s开始准备做包子啦!"%name)
    for i in range(10):
        time.sleep(1)
        print("做了1个包子,分两半!")
        c.send(i)    #send可以传值给yield，然后进一步将值传给baozi
        c2.send(i)

producer("alex")