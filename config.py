params = {
  # crypto setup
  'currency_1': 'BTC', # Bitcoin
  'currency_2': 'ETH', # Ethereum
  'currency_3': 'LINK', # Chainlink
  'ref_currency': 'USD',
  'ma': 25,
  # api setup
  'api_call_period': 5,
}

config = {
  # kafka
  'kafka_broker': 'localhost:9092',
  # topics
  'topic_1': 'topic_{0}'.format(params['currency_1']),
  'topic_2': 'topic_{0}'.format(params['currency_2']),
  'topic_3': 'topic_{0}'.format(params['currency_3']),
  'topic_4': 'topic_{0}_ma_{1}'.format(params['currency_1'], params['ma']),
  'topic_5': 'topic_{0}_ma_{1}'.format(params['currency_2'], params['ma']),
  'topic_6': 'topic_{0}_ma_{1}'.format(params['currency_3'], params['ma']),
}