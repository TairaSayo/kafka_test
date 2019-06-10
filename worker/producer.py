from kafka import KafkaProducer
import time
from time import sleep
from prometheus_client import start_http_server, Summary

producer = KafkaProducer(bootstrap_servers=['kafka:9092'], 
                        client_id='worker_producer')
topic = "input"

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@REQUEST_TIME.time()
def produce_request():
    i = str(int(time.time() * 1000))
    producer.send(topic, value=i)
    sleep(1)

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        produce_request()