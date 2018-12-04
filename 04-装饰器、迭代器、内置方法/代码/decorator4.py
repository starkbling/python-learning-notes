__author__ = "Alex Li"
import time
def timer(func): #timer(test1)  func=test1
    def deco(*args,**kwargs):  #能够传递任意数量的参数，满足调用test1无参数和test2两个参数
        start_time=time.time()
        func(*args,**kwargs)   #run test1()
        stop_time = time.time()
        print("the func run time  is %s" %(stop_time-start_time))
    return deco
@timer  #相当于test1=timer(test1)
def test1():
    time.sleep(1)
    print('in the test1')

@timer # test2 = timer(test2)  = deco  test2(name) =deco(name)
def test2(name,age):
    time.sleep(2)
    print("test2:",name,age)

test1()
test2("alex",22)