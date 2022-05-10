import time, json
import numpy as np
import datetime as dt

from kafka import KafkaProducer, KafkaConsumer
from config import config


def initProducer():
    # init an instance of KafkaProducer
    print('Initializing Kafka producer at {}'.format(dt.datetime.utcnow()))
    producer = KafkaProducer(
      bootstrap_servers=config['kafka_broker'],
      value_serializer=lambda v: json.dumps(v, default=str).encode('utf-8')
    )
    print('Initialized Kafka producer at {}'.format(dt.datetime.utcnow()))
    return producer


def initConsumer(topic, timeout=1000):
    # init an instance of KafkaConsumer
    consumer = KafkaConsumer(topic, bootstrap_servers=config['kafka_broker'], group_id=None,
        auto_offset_reset='earliest', enable_auto_commit=False, consumer_timeout_ms=timeout,
        value_deserializer=lambda m: json.loads(m.decode('utf-8')))
    return consumer


def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)
    # handle exception


def produceRecord(data, producer, topic, partition=0):
    # act as a producer sending records on kafka
    # print("hello?")
    # future = producer.send(topic=topic, partition=partition, value=data)
    # try:
    #     record_metadata = future.get(timeout=10)
    # except KafkaError:
    #     # Decide what to do if produce request failed...
    #     log.exception()
    #     pass

    # produce json messages
    # produce asynchronously with callbacks
    producer.send(topic=topic, partition=partition, value=data).add_callback(on_send_success).add_errback(on_send_error)

    # debug \ message in prompt
    print('Produce record to topic \'{0}\' at time {1}'.format(topic, dt.datetime.utcnow()))

def consumeRecord(consumer):
    rec_list = []
    # append to list any new records in consumer
    for rec in consumer:
        r = rec.value
        rec_list.append(r)
    # return list of new records
    return rec_list
