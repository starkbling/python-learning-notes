# -*- coding:utf-8 -*-
__Author__ = 'BLINGBLING'
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

result = channel.queue_declare(exclusive=True) #排他性质的
queue_name = result.method.queue

severities = sys.argv[1:]   #此处是运行该脚本时候输入的参数值
print(severities)
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])  #在终端打印需要输入的参数类型
    sys.exit(1)

for severity in severities:
    channel.queue_bind(exchange='direct_logs',
                      queue = queue_name,
                      routing_key=severity)   #指定接收消息时候的key值

def callback(ch, method, properties, body):
    """键的回调函数，在收到消息之后如何对消息进一步处理，该函数存在非常大的扩展空间"""
    print(" [x] %r:%r" % (method.routing_key, body))

print(' [*] Waiting for logs. To exit press CTRL+C')
channel.basic_consume(callback,
                      queue = queue_name,
                      no_ack = True)

channel.start_consuming() #挂起等待收取消息