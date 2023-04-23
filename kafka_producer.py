from kafka import KafkaProducer

data=input('Enter your message')

b_data=bytes(data,encoding='utf-8')


from threading import Thread



producer= KafkaProducer(bootstrap_servers='localhost:9092')
i=0
while True:
    i+=1
    # key is set to None so as to auto assign partitioner to send message to
    producer.send('topicOne',key=None,value=b_data,)
    print('done')
    if(i==5):
        break
producer.flush()

