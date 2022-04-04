from time import sleep  
from json import dumps  
from kafka import KafkaProducer  
import logging

# initializing the Kafka producer
my_producer = KafkaProducer(
    bootstrap_servers = ['localhost:9092'],
    value_serializer = lambda x:dumps(x).encode('utf-8')  
    )

def s_producer(topic, my_data):
# generating the numbers ranging from 1 to 500
    for n in range(500):
        print("FROM PRODUCE")
        print(my_data)
        my_producer.send(topic, value = my_data)  
        sleep(5)
        my_producer.flush()

# This is the test to run
# Used static data - examples coment it and coment out the test you want to test.
# topic = 'dev.pingpong.requested'
# my_data = {"transaction-id": "ID01", "payload": {"message": "ping"}}    
# s_producer(topic=topic, my_data=my_data)

topic = 'dev.pingpong.requested'
my_data = {"transaction-id": "ID01", "payload": {"message": "ping"}}
# my_data = {"transaction-id": "ID01", "payload": {"message": "abc"}}
# my_data = {"transaction-id": "ID01", "payload": {"abc"}}
s_producer(topic=topic, my_data=my_data)

