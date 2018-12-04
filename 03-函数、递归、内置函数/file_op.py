__author__ = "Alex Li"
import sys
import time
'''
#data = open("yesterday",encoding="utf-8").read()
f = open("yesterday2",'a',encoding="utf-8") #文件句柄
#a = append 追加

f.write("\nwhen i was young i listen to the radio\n")
data = f.read()
print('--read',data)

f.close()
'''


#注意用w则会创建新的文件，如果有同名的文件那么原文件就会覆盖掉
f = open("yesterday2",'r+',encoding="utf-8")
#文件句柄 读写，先打开对应的文件，能读也能写，写的内容只会加在最后，比较有用
f = open("yesterday2",'w+',encoding="utf-8")
#文件句柄 写读，先创建一个新的文件，能写也能读，写的内容也是放在了最后
f = open("yesterday2",'a+',encoding="utf-8") #文件句柄 追加读写，能读也能写

#二进制文件处理
f = open("yesterday2",'wb') #文件句柄  二进制文件，如视频和图片等
f = open("yesterday2",'rb') #文件句柄  二进制文件，如视频和图片等，主要用于网络传输
f.write("hello binary\n".encode()) #将字符串转换为二进制类型数据


'''

print(f.encoding)

#print(f.flush())
print(dir(f.buffer) )
#high bige

count = 0
for line in f:
    if count == 9:
        print('----我是分割线----------')
        count += 1
        continue
    print(line)
    count +=1

#low loop

for index,line in enumerate(f.readlines()):
    if index == 9:
        print('----我是分割线----------')
        continue
    print(line.strip())
#for i in range(5):
#    print(f.readline())
'''
for i in range(30):
    sys.stdout.write("#")
    sys.stdout.flush() #及时显示出来
    time.sleep(0.1)

f.truncate(10) #从头开始截断，如果括号里面什么都不写，就是从0，那么文件就会全部清空了，n表示只截留前面的十个字符。后面的全部不保留
f.close()
#
f = open("yestreday2","r",encoding="utf-8")
f_new = open("yesterday.bac","w",encoding="utf-8")
#修改原文件的一段话，生成一个新的文件来保存原来的修改
for line in f:
    if "肆意的快乐等我享受" in line:
        line = line.replace("肆意的快乐等我享受","肆意的快乐等Bling享受")
    f.write(line)
f.close()
f_new.close()
#可以用with管理文件，with可以打开多个文件
with open("log1") as obj1,open("log2") as obj2:
    pass