__author__ = "Alex Li"

import os

class Dog(object):
    '''这个类是描述狗这个对象的'''

    def __init__(self,name):
        self.name = name
        self.__food = None

    #@staticmethod #实际上跟类没什么关系了
    #@classmethod
    @property  #attribute，属性的意思,属性方法默认是没法删除的
    def eat(self):
        print("%s is eating %s" %(self.name,self.__food))
    @eat.setter     #设置私有属性
    def eat(self,food):
        print("set to food:",food)
        self.__food = food    #私有的方法

    @eat.deleter     #删除私有属性
    def eat(self):
        del self.__food  #删除self.__food属性
        print("删完了")

    def talk(self):
        print("%s is talking"% self.name)

    def __call__(self, *args, **kwargs):  #这样就可以创造callable对象
        print("running call",args,kwargs)

    def __str__(self):
        return "<obj:%s>" %self.name


print(Dog.__doc__)   #打印类的描述信息

d = Dog("ChenRonghua")
d("哈哈",1,2, a = 1,b=2)   #使用d()方法，传入元组或者字典
d.eat = "baozi"
d.eat
del d.eat    #删除私有属性
d.eat = "jiaozi"
d.eat
# print(d)
# print(Dog.__dict__) #打印类里的所有属性，不包括实例属性，数据类型为字典
# print(d.__dict__) #打印所有实例属性，不包括类属性，数据类型为字典
# d(1,2,3,name=333)
#Dog("ChenRonghua")()
