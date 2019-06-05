from kafka import KafkaProducer
import time
from time import sleep

producer = KafkaProducer(bootstrap_servers=['kafka:9092'], 
                        client_id='worker_producer')
topic = "input"

while True:
    i = str(int(time.time() * 1000))
    producer.send(topic, value=i)
    sleep(1)