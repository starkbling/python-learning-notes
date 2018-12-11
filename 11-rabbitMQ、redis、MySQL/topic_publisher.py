# -*- coding:utf-8 -*-
__Author__ = 'BLINGBLING'
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='topic_logs',
                         exchange_type="topic")

routing_key = sys.argv[1] if len(sys.argv) > 1 else "anonymous.info"
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange = 'topic_logs',
                      routing_key=routing_key,  #用于识别的关键key，消费的程序根据这个来识别是否接受消息
                      body = message)

print(" [x] Sent %r:%r" % (routing_key, message))
channel.close()