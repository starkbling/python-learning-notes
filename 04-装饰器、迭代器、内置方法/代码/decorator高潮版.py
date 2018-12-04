#-*- coding:utf-8 -*-
__author__ = "Alex Li"
import time
user,passwd = 'alex','abc123'
def auth(auth_type):
    # print("auth func:",auth_type)
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            print("wrapper func args:", *args, **kwargs)
            if auth_type == "local":
                username = input("Username:").strip()
                password = input("Password:").strip()
                if user == username and passwd == password:
                    print("\033[32;1mUser has passed authentication\033[0m") #输出绿色字体
                    res = func(*args, **kwargs)  # from home在此，res为home()的执行结果
                    print("---after authenticaion ")
                    return res  #此处获取home()执行之后的返回值
                else:
                    exit("\033[31;1mInvalid username or password\033[0m") #输出红色字体
            elif auth_type == "ldap":
                print("搞毛线ldap,不会。。。。")

        return wrapper
    return outer_wrapper

def index(number):
    print("welcome to index page %s"%number)

@auth(auth_type="local") # home = wrapper()，给装饰器传递相应的参数来实现
def home(name):
    print("%s welcome to home  page"%name)
    return "from home"  #思考如何获取home()的执行结果

@auth(auth_type="ldap")
def bbs(pages):
    print("welcome to bbs %s page"%pages)

index(12)
print(home("guest")) #wrapper()
bbs(11)