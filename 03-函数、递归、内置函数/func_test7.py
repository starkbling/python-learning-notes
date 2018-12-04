__author__ = "Alex Li"

#*args:接受N个位置参数，转换成元组形式，针对实参不固定的情况，只要以“*”号开头就行，后面随便命名
def test(*args):
    print(args)

test(1,2,3,4,5,5)
test(*[1,2,4,5,5])  #  args=tuple([1,2,3,4,5])

#位置函数和任意函数一起使用
def test1(x,*args):
    print(x)
    print(args)

test1(1,2,3,4,5,6,7)


#**kwargs：接受N个关键字参数，转换成字典的方式
def test2(**kwargs):
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['age'])
    print(kwargs['sex'])

test2(name='alex',age=8,sex='F')
test2(**{'name':'alex','age':8}) #此种方式也是可以的，输出字典，函数内部也可以调用字典的各个值
def test3(name,**kwargs):
    print(name)
    print(kwargs)

# test3('alex',{"age":18,"sex":'m'}) #这种方式是没法用的，必须是age=18，sex=m 这种形式
test3('alex',**{"age":18,"sex":'m'}) #这种方式可以用

位置参数、默认参数、字典参数可以一起使用，字典参数可以不指定
def test4(name,age=18,**kwargs):
    print(name)
    print(age)
    print(kwargs)

test4('alex',sex='m',hobby='tesla',age=3) #给默认参数赋值可以用位置参数形式赋值，也可以关键字参数赋值，如age=3

def test4(name,age=18,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
    logger("TEST4")

#*args接受的是位置参数

def logger(source):
    print("from %s" %  source)
#
test4('alex',age=34,sex='m',hobby='tesla') #test4的调用需要放在logger函数后面，因test4函数中调用了logger函数


