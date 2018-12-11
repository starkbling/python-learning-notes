# -*- coding:utf-8 -*-
"""消费者接收消息是论询的机制，按启动的时间顺序轮流接收消息"""
__Author__ = 'BLINGBLING'
import pika,time

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
    )
channel = connection.channel() #声明一个管道

# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
channel.queue_declare(queue='hello',durable=True)  #再声明一个队列,由于不确定是生产者还是消费者先运行，所以都需要先声明一个队列


def callback(ch, method, properties, body):  #回调函数，消息来了就调用该函数
    """:param ch 管道的内存对象地址
    :param method 消息传递的相关参数，定义消息的内容，在脚本运行的后面传入的参数，能够定义用什么方式处理消息
    具体的用法可见后面的fanout、direct和topic等消息处理
    :param properties
    """
    print("-->:",ch)
    # time.sleep(20)
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)  #该方法用于手动向服务器反馈消息，表明消息已经处理完毕

channel.basic_qos(prefetch_count=1)
# 在各个消费者端，配置perfetch=1,意思就是告诉RabbitMQ在我这个消费者当前消息还没处理完的时候就不要再给我发新消息了
channel.basic_consume(                                         #消费消息
                    callback, #如果收到消息，就调用该函数来处理消息
                    queue='hello',
)# make message persistent

                    # no_ack=True)  #no acknowledgement 不给服务器端发消息，告诉该消息是否处理完，默认是False

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()  #开始收集消息