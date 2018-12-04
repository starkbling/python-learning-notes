from multiprocessing import Process
import os

def info(titile):
    print(titile)
    print('module name:',__name__)
    print("parent process:",os.getppid()) #获取父进程的id
    print('process id:',os.getpid())   #获取本进程的pid
    print('************************')

def f(name):
    info('\033[31;1mCalled from function f child Process Function\033[0m')
    print('hello',name)

if __name__ =='__main__':
    info('\033[32;1mMain pross line\033[0m')
    p =Process(target=f,args=('bbo',))
    p.start()
    f('bling') #每一个进程都默认有一个父进程，terminal为系统终端进程