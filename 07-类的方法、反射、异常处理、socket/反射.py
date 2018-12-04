__author__ = "Alex Li"

def bulk(self):
    print("%s is yelling...." %self.name)

class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating..."%self.name,food)


d = Dog("NiuHanYang")
choice = input(">>:").strip()

if hasattr(d,choice):
    delattr(d,choice)   #删除对象d对应的名称为choice的属性
    # setattr(d,choice,"bling")
    # print(getattr(d, choice))

else:
    setattr(d,choice,"Hello!")   #d.talk = None
    print(getattr(d,choice))  #返回属性值str
    # setattr(d,choice,bulk) #d.talk = bulk
    # func = getattr(d, choice)
    # func(d)
print(d.name)
