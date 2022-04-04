from json import loads  
from kafka import KafkaConsumer  
from kafka import KafkaProducer
from json import dumps  
from schema import Schema, And, Use, Optional, SchemaError
import logging

# This can be taken from env variables. 
topic = 'dev.pingpong.requested'
success_topic = 'dev.pingpong.succeeded'
failed_topic = 'dev.pingpong.failed'

# initializing the Kafka producer
my_producer = KafkaProducer(
    bootstrap_servers = ['localhost:9092'],
    value_serializer = lambda x:dumps(x).encode('utf-8')  
    )

def check(conf_schema, conf):
    try:
        conf_schema.validate(conf)
        return True
    except SchemaError:
        return False

conf_schema = Schema({
    'transaction-id': And(Use(str)),
    'payload': {
        'message': And(Use(str)),
    }
})

# generating the Kafka Consumer  
# my_consumer = KafkaConsumer(  
#      topic,  
#      bootstrap_servers = ['localhost : 9092'],  
#     #  auto_offset_reset = 'earliest', 
#      auto_offset_reset = 'latest',
#      enable_auto_commit = True,  
#      group_id = 'my-group',  
#      value_deserializer = lambda x : loads(x.decode('utf-8'))  
#      )  

# my_client = MongoClient()
# my_collection = my_client.testnum.testnum  

# Connection via localhost - docker
consumer = KafkaConsumer(
    topic, 
    bootstrap_servers=['localhost : 9092'], 
    group_id='my-group', 
    enable_auto_commit=True,
    value_deserializer = lambda x : loads(x.decode('utf-8'))
    )


# def read_consumer(consumer):
consumer.poll()
# go to end of the stream
consumer.seek_to_end()
for message in consumer:
    message = message.value
    print(message)
    if check(conf_schema, message):
        if message["payload"]['message'] == 'ping':
            message["payload"]['message'] = 'pong'
            print("Message send to PONG")
            my_producer.send(success_topic, value = message)  
            my_producer.flush()
        elif message["payload"]['message'] != 'ping':
            print("Message FAILED")
            message["payload"]['message'] = "Error the message doesn't contain 'ping'"
            my_producer.send(failed_topic, value = message)  
            my_producer.flush()
    else:
        print("Schema not properly set")
        message_error = {"transaction-id": "ID01", "payload": {"message": "Error in the format of the Kafka event"}}
        my_producer.send(failed_topic, value = message_error)  
        my_producer.flush()