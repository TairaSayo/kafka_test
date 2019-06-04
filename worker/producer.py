from kafka import KafkaProducer
from kafka.errors import KafkaError
import time

producer = KafkaProducer(bootstrap_servers=['kafka:9092'])
topic = "input"

while true:
    i = int(round(time.time() * 1000))
    producer.send(topic, value=b'i' )