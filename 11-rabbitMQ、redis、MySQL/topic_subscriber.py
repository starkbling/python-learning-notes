# -*- coding:utf-8 -*-
__Author__ = 'BLINGBLING'
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange_type='topic',
                         exchange='topic_logs')
result = channel.queue_declare(exclusive=True) #保证生成的queue是唯一的，会自动消除
queue_name = result.method.queue

bulding_keys = sys.argv[1:]  #新建一个独一无二的可以和publisher中的routing_key 相匹配
if not bulding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for bulding_key in bulding_keys:  #给queue绑定key
    channel.queue_bind(queue = queue_name,
                       routing_key=bulding_key,
                       exchange='topic_logs')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

print(' [*] Waiting for logs. To exit press CTRL+C')
channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)
channel.start_consuming()