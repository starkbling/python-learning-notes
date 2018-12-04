__author__ = "Alex Li"

import configparser

conf = configparser.ConfigParser()      #定义一个config对象
conf.read("example.ini")        #读取一个config文件

print(conf.defaults())      #读取defauls节点的数据
print(conf['bitbucket.org']['user'])    #获取对应节点下的内容
print(conf.sections())   #获取节点名，不包括defaults节点
sec = conf.remove_section('bitbucket.org')
conf.write(open('example1.ini', "w"))