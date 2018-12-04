#-*-coding:gbk-*-

import sys
print(sys.getdefaultencoding())
__author__ = "Alex Li"

s = "你哈"  #s是unicode编码，python程序默认编码是unicode，所以s.decode 没法用，因为s已经是unicode编码了
print(s.encode("gbk").decode("gbk")) #这样就能显示中文“你哈”
print(s.encode("utf-8"))
print(s.encode("utf-8").decode("utf-8").encode("gb2312"))


