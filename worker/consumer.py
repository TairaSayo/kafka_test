from kafka import KafkaProducer
from kafka import KafkaConsumer
import time


producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                        client_id='worker_consumer')
input_topic = "input"
output_topic = "output"


consumer = KafkaConsumer(
    input_topic,
     bootstrap_servers=['kafka:9092'],
     auto_offset_reset='earliest',
     client_id='worker_consumer',
     enable_auto_commit=True)

for message in consumer:
    i = time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(float(message.value)/1000))
    producer.send(output_topic, value=i)