__author__ = "Alex Li"

from lib.aa import C

obj = C()
print(obj.__module__)     # 输出 lib.aa，即：输出模块
print(obj.__class__ )     # 输出 lib.aa.C，即：输出类


class Foo(object):
    def __init__(self):
        self.name = 'wupeiqi'

    def func(self):
        return 'func'


obj = Foo()

# #### 检查是否含有成员 ####
hasattr(obj, 'name')
hasattr(obj, 'func')

# #### 获取成员 ####
getattr(obj, 'name')
getattr(obj, 'func')

# #### 设置成员 ####
setattr(obj, 'age', 18)
setattr(obj, 'show', lambda num: num + 1)
print(obj.show(3))

# #### 删除成员 ####
delattr(obj, 'name')








