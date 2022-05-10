# Using Redpanda to Track Cryptocurrency Price Trends

This repo polls Coinbase API for various cryptocurrency prices and uses [Redpanda](https://redpanda.com/) to calculate moving average prices and stores the data in a timeseries database, [QuestDB](https://questdb.io/), for further analysis.

## Prerequisites

- Docker (min of 4GB memory)
- Python 3.7+

Note: the Kafka Connect image is compiled for AMD64 architecture. While Docker may utilize Rosetta 2 to run AMD64 images on ARM64 architectures (e.g. Mac M1), it may have degraded performance.

## Structure

- docker-compose: holds docker-compose file to start Redpanda, QuestDB, and JSON file to initialize Kafka Connect
- docker: Dockerfile to build Kafka Connect image (if you wish to build locally or extend)
- Python files:
  - config.py: specify polling frequency, cryptocurrency
  - getData.py: polls Coinbase API and publishes records to Kafka
  - kafkaHelper.py: wrapper around kafka-python lib
  - movingAverage.py: calculates a moving average per cryptocurrency

## Quickstart

### Redpanda/QuestDB Setup

Start up the Redpanda/QuestDB stack:

```
cd docker-compose
docker-compose up -d
```

Wait until all the components are healthy (look at Kafka Connect container logs).

Post postgres-sink-btc schema to Kafka Connect:

```
curl -X POST -H "Accept:application/json" -H "Content-Type:application/json" --data @postgres-sink-btc.json http://localhost:8083/connectors
```

### Python Setup

Install the necessary packages:

```
pip install -r requirements.txt
```

Run the script to poll Coinbase API:

```
python getData.py
```

(Optional): calculate moving averages

```
python movingAverage.py
```
