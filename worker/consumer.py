from kafka import KafkaProducer
from kafka import KafkaConsumer
import time
from prometheus_client import start_http_server, Summary

producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                        client_id='worker_consumer')
input_topic = "input"
output_topic = "output"

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

consumer = KafkaConsumer(
    input_topic,
     bootstrap_servers=['kafka:9092'],
     auto_offset_reset='earliest',
     client_id='worker_consumer',
     enable_auto_commit=True)

@REQUEST_TIME.time()
def consume_request():
    i = time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(float(message.value)/1000))
    producer.send(output_topic, value=i)

if __name__ == '__main__':
    start_http_server(8100)
    for message in consumer:
        consume_request()