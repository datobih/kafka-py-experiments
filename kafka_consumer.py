from kafka import KafkaConsumer

# consumer=KafkaConsumer('topic_one',bootstrap_servers='localhost:9092',auto_offset_reset='earliest')
# print('doings')
# for msg in consumer:
#     print(msg.value)
#     print(msg.partition)

#     # consumer.commit()

# print('done')
# consumer.close()

from multiprocessing import Process
import os
def consume():
    consumer=KafkaConsumer('topicOne',bootstrap_servers='localhost:9092',auto_offset_reset='earliest',group_id='group_one')
    print('doings')
    for msg in consumer:
        pid = os.getpid()
        print(pid)
        print(msg.value)
        print(msg.partition)
        consumer.commit()
    print('done')

if __name__=='__main__':
    # Create two consumers
    Process(target=consume).start()
    Process(target=consume).start()