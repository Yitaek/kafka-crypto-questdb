import asyncio
from getData import async_getCryptoRealTimeData
from kafkaHelper import initProducer
from config import config, params

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
asyncio.run()