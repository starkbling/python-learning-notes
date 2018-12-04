__author__ = "Alex Li"

import os


class Dog(object):
    n = 333   #这里面的变量才能够被类变量调用
    name = "huazai"
    def __init__(self,name):
        self.name = name
    @classmethod  #类方法中只能访问类变量，不能访问实例变量
    def eat(self):
        print("%s is eating %s" %(self.name,'dd'))  #self.name = "huazai"
    def talk(self):
        print("%s is talking"% self.name)

Dog.name = "mumu"
d = Dog("ChenRonghua")
d.eat()
