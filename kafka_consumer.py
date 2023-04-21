from kafka import KafkaConsumer

consumer=KafkaConsumer('test',bootstrap_servers='localhost:9092',auto_offset_reset='earliest',consumer_timeout_ms=1000,group_id='my-group')
print('doings')
for msg in consumer:
    print(msg.value)

    consumer.commit()

print('done')
consumer.close()