import pandas as pd 
import numpy as np 
import datetime as dt

from kafkaHelper import produceRecord, consumeRecord, initConsumer, initProducer
from config import config, params

# initialize Kafka consumers and producer
print('Starting Apache Kafka consumers and producer')
consumer_1 = initConsumer(config['topic_1'])
consumer_2 = initConsumer(config['topic_2'])
consumer_3 = initConsumer(config['topic_3'])
producer = initProducer()

# intialize local dataframe
data_1 = pd.DataFrame(columns=['time', 'value'])
data_2 = pd.DataFrame(columns=['time', 'value'])
data_3 = pd.DataFrame(columns=['time', 'value'])

while True:
    # consume data from Kafka
    # topic 1 --> 4
    records_1 = consumeRecord(consumer_1)
    print('Consume record from topic \'{0}\' at time {1}'.format(config['topic_1'], dt.datetime.utcnow()))
    for r in records_1:
        dt_obj = dt.datetime.strptime(r['payload']['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
        data_1.loc[len(data_1)] = [int(dt_obj.timestamp() * 1000), float(r['payload']['amount'])]
        ma_1 = {'timestamp': r['payload']['timestamp'], 'amount': float(data_1['value'].tail(n=params['ma']).mean())}
        # produce data
        produceRecord(ma_1, producer, config['topic_4'])
        print('Produce record to topic \'{0}\' at time {1}'.format(config['topic_4'], dt.datetime.utcnow()))

    # topic 2 --> 5
    records_2 = consumeRecord(consumer_2)
    print('Consume records from topic \'{0}\' at time {1}'.format(config['topic_2'], dt.datetime.utcnow()))
    for r in records_2:
        dt_obj = dt.datetime.strptime(r['payload']['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
        data_2.loc[len(data_2)] = [int(dt_obj.timestamp() * 1000), float(r['payload']['amount'])]
        ma_2 = {'timestamp': r['payload']['timestamp'], 'amount': float(data_2['value'].tail(n=params['ma']).mean())}
        # produce data
        produceRecord(ma_2, producer, config['topic_5'])
        print('Produce record to topic \'{0}\' at time {1}'.format(config['topic_5'], dt.datetime.utcnow()))

    # topic 3 --> 6
    records_3 = consumeRecord(consumer_3)
    print('Consume records from topic \'{0}\' at time {1}'.format(config['topic_3'], dt.datetime.utcnow()))
    for r in records_3:
        dt_obj = dt.datetime.strptime(r['payload']['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
        data_3.loc[len(data_3)] = [int(dt_obj.timestamp() * 1000), float(r['payload']['amount'])]
        ma_3 = {'timestamp': r['payload']['timestamp'], 'amount': float(data_3['value'].tail(n=params['ma']).mean())}
        # produce data
        produceRecord(ma_3, producer, config['topic_6'])
        print('Produce record to topic \'{0}\' at time {1}'.format(config['topic_6'], dt.datetime.utcnow()))