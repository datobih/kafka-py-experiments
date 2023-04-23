# from threading import Thread
# class KafkaThread(Thread):
#     daemon=True

# import time

#     def run(self):
#         import time
        # consumer=KafkaConsumer('test',
        #                        bootstrap_servers='localhost:9092',
        #                        group_id='my-group',
        #                        auto_offset_reset='earliest'
        #                        )
        # for message in consumer:
        #     print(message.value)
# while True:
#     print('hey')
#     time.sleep(3)


# KafkaThread().start()


import os
import django
from kafka import KafkaConsumer
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'microservice_one.settings')
django.setup()

def consume():
    from consumer_app.models import Message
    consumer= KafkaConsumer('topicOne',bootstrap_servers='localhost:9092',auto_offset_reset='earliest',group_id='group_one')
    for msg in consumer:
        #Get process id of current consumer
        pid = os.getpid()
        print(pid)
        print(msg.value)
        print(msg.partition)
        message=Message()
        message.text=(msg.value).decode('utf-8')
        message.save()
        consumer.commit()
        print(f"saved {msg.value}")

if (__name__=='__main__'):
    from multiprocessing import Process
    Process(target=consume).start()


        