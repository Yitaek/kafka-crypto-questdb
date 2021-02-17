import json, requests, time, asyncio
import numpy as np
import datetime as dt

from kafkaHelper import initProducer, produceRecord
from config import config, params

# real time data collector
async def async_getCryptoRealTimeData(producer, topic, crypto, time_inverval):
    while True:
        t_0 = time.time()
        # call API
        uri = 'https://api.coinbase.com/v2/prices/{0}-{1}/{2}'.format(crypto, params['ref_currency'], 'spot')
        res = requests.get(uri)

        if (res.status_code==200):
            # read json response
            raw_data = json.loads(res.content)
       
            # add schema
            new_data = {
              "schema": {
                "type": "struct",
                "fields": [
                  {
                    "type": "string",
                    "optional": False,
                    "field": "currency"
                  },
                  {
                    "type": "float",
                    "optional": False,
                    "field": "amount"
                  },
                  {
                    "type": "string",
                    "optional": False,
                    "field": "timestamp"
                  }
                ],
                "optional": False,
                "name": "coinbase"
              },
              "payload": {
                "timestamp": dt.datetime.utcnow(),
                "currency": raw_data['data']['base'],
                "amount": float(raw_data['data']['amount'])
              }
            }    

            # debug / print message
            print('API request at time {0}'.format(dt.datetime.utcnow()))
            # produce record to kafka
            produceRecord(new_data, producer, topic)
            # debug \ message in prompt
            # print('Produce record to topic \'{0}\' at time {1}'.format(topic, dt.datetime.utcnow()))
            
            print('Record: {}'.format(new_data))
            
        else:
            # debug / print message
            print('Failed API request at time {0}'.format(dt.datetime.utcnow()))
        # wait
        await asyncio.sleep(time_inverval - (time.time() - t_0))

# initialize kafka producer
producer = initProducer()

# define async routine
async def main():
    await asyncio.gather(
    async_getCryptoRealTimeData(producer, config['topic_1'], params['currency_1'], params['api_call_period']),
    async_getCryptoRealTimeData(producer, config['topic_2'], params['currency_2'], params['api_call_period']),
    async_getCryptoRealTimeData(producer, config['topic_3'], params['currency_3'], params['api_call_period'])
)
# run async routine
asyncio.run(main())