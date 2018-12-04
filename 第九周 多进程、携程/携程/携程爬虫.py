# -*- coding:utf-8 -*-
__Author__ = 'BLINGBLING'

from gevent import monkey
monkey.patch_all()   #把当前程序的所有的io操作给我单独的做上标记，自动检测是否进行了io操作
import gevent,time
from urllib.request import urlopen


def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

ts = time.time()
gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/'),
])   #串行运行，遇到io操作的时候自动切换到另外的函数运行
print("time spending %s"%(time.time() - ts))