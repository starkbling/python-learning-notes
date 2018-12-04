__author__ = "Alex Li"
#函数即变量

#示范一：
# def foo():
#     print('in the foo')
# foo()

#示范二：
def bar():
    print('in the bar')
def foo():
    print('in the foo')
    bar()
foo()

#示范三：
def foo():
    print('in the foo')
    bar()
def bar():  #bar的函数位置发生了变化，但是在调用之前
    print('in the bar')
foo()

#示范四：
# def foo():
#     print('in the foo')
#     bar()
#foo()   #bar函数放在了调用之后，因此运行不了
# def bar():
#     print('in the bar')

