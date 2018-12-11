# -*- coding:utf-8 -*-
__Author__ = 'BLINGBLING'

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()

# 声明queue
channel.queue_declare(queue='hello',durable=True)  #durable 声明对消息进行持久化
#durable持久化的时候，只会将队列持久化

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello',#queue名字
                      body='Hello World!',
                      properties=pika.BasicProperties( delivery_mode=2, )  #发送的消息也进行持久化
                       )
print(" [x] Sent 'Hello World!'")
connection.close()