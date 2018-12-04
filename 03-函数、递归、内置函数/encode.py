import sys
print(sys.getdefaultencoding())
__author__ = "Alex Li"

s = "你好"
s_gbk = s.encode("gbk") #encode会将原来的字符转换为字节bytes类型

print(s_gbk)
print(s.encode())  #将字符转换为bytes类型

gbk_to_utf8 = s_gbk.decode("gbk").encode("utf-8") #decode中的括号是告诉程序字符类型
print("utf8",gbk_to_utf8)

#uncode编码打印的时候，如果是元组，那么显示的是编码
"""
s= "你好"
s_to_unicode = s.decode("utf-8") #将utf-8转换为unicode
s_to_gbk = s_to_unicode.encode("gbk") #将unicode转换为utf-8
gbk_to_utf8 = s_gbk.decode("gbk").encode("utf-8")  #将gbk先用decode解码为unicode，然后再编码为utf—8

#unicode 和utf-8之间是可以直接打印的
s1 = u"你好"  #这样写，那么s1就表明是用unicode编码了
"""