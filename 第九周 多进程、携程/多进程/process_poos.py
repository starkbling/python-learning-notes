# -*- coding=utf-8 -*-
__Author__ = 'BLINGBLING'
from multiprocessing import Pool
import os,time

def foo(i):
    time.sleep(2)
    print("Hello, %s:%s"%(i,os.getpid()))
    return os.getpid()   #此处返回的值将会传入到back的参数中

def back(args):
    print("%s done."%args)

if __name__=="__main__":
    poo = Pool(processes=6)
    for i in range(12):
        poo.apply_async(func = foo, args=(i,),callback=back)
    poo.close()  #必须先调用close 然后再调用join
    poo.join()