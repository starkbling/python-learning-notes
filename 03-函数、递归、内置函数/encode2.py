#-*-coding:gbk-*-

import sys
print(sys.getdefaultencoding())
__author__ = "Alex Li"

s = "���"  #s��unicode���룬python����Ĭ�ϱ�����unicode������s.decode û���ã���Ϊs�Ѿ���unicode������
print(s.encode("gbk").decode("gbk")) #����������ʾ���ġ������
print(s.encode("utf-8"))
print(s.encode("utf-8").decode("utf-8").encode("gb2312"))


