__author__ = "Alex Li"

import configparser #ConfigParser

config = configparser.ConfigParser()  #处理的对象

config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}  #第一个节点，设置默认的值

config['bitbucket.org'] = {} #第二个节点
config['bitbucket.org']['User'] = 'hg'

config['topsecret.server.com'] = {}  #第三个节点
config['topsecret.server.com']
config['topsecret.server.com']['Host Port'] = '50022'  # mutates the parser
config['topsecret.server.com']['ForwardX11'] = 'no'  # same here

config['DEFAULT']['ForwardX11'] = 'yes' #在第一个节点加入内容


with open('example.ini', 'w') as configfile:
    config.write(configfile)