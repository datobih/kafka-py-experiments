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
if (__name__=='__main__'):
    from django.contrib.auth import get_user_model
    from consumer_app.models import Message
    consumer= KafkaConsumer('topic_one',bootstrap_servers='localhost:9092',auto_offset_reset='earliest',group_id='my-group')
    for msg in consumer:
        message=Message()
        message.text=(msg.value).decode('utf-8')
        message.save()
        print(f"saved {msg.value}")

        