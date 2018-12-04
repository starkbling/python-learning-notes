__author__ = "Alex Li"

import time
def timmer(func):
    def warpper(*args,**kwargs):
        start_time=time.time()
        func()
        stop_time=time.time()
        print('the func run time is %s' %(stop_time-start_time))
    return warpper

@timmer  #运行装饰器
def test1():
    time.sleep(1)
    print('in the test1')

test1()