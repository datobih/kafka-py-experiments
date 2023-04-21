from kafka import KafkaProducer

data=input('Enter your message')

b_data=bytes(data,encoding='utf-8')


producer= KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('test',key=b'test_producer',value=b_data)
print('done')
producer.flush()