__author__ = "Alex Li"


school = "Oldboy edu."
names = ["Alex","Jack","Rain"] # 字符串和整体型的数据等全局变量，在不加global时没法在函数里面修改
#但是比如列表、字典、集合和类等的全局变量类型在不加global的时候函数也能修改
names_tuple = (1,2,3,4)
def change_name():
    names[0] = "金角大王"
    print("inside func",names)
change_name()
print(names)


def change_name(name):
    global school  #将局部变量school变成全局变量，这样函数能够改变全局变量的值
    print("before change",name,school)
    school = "Mage Linux"
    name ="Alex li" #这个函数就是这个变量的作用域，全局变量里面的name并没有发生改变
    # age =23
    print("after change",name,school)


print("before change school name:",school)

name = "alex"
change_name(name)
print(name)
print("after change school name:",school)
#print("age",age)

