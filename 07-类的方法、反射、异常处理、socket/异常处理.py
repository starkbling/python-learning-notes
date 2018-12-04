__author__ = "Alex Li"

def bulk(self):
    print("%s is yelling...." %self.name)

class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating..."%self.name,food)


#
# d = Dog("NiuHanYang")
# choice = input(">>:").strip()
# getattr(d,choice)



names = ['alex','jack']
# names['sdfsdf']
# data = {}
#
#
try:
    open("tes.txt")

except (KeyError,IndexError) as e :
    print("没有这个key",e)
except IndexError as e :
    print("列表操作错误",e)
except Exception as e:
    print("其他错误",e)
except BaseException as e:
    print("未知错误",e)
else:
    print("一切正常的时候才执行")
finally:
    print("不管有没有错，都执行")

try:
    # 主代码块
    pass
except KeyError as e:
    # 异常时，执行该块
    pass
else:
    # 主代码块执行完，执行该块
    pass
finally:
    # 无论异常与否，最终执行该块
    pass