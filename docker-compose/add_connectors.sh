#!/usr/bin/env bash
curl -G \
  --data-urlencode 'query=CREATE TABLE IF NOT EXISTS coinbase (currency symbol CAPACITY 1000 INDEX, amount float, `timestamp` timestamp) TIMESTAMP("timestamp") PARTITION BY DAY;'\
  http://localhost:9000/exec
curl -G \
  --data-urlencode 'query=CREATE TABLE IF NOT EXISTS moving_averages (currency symbol CAPACITY 1000 INDEX, amount float, `timestamp` timestamp) TIMESTAMP("timestamp") PARTITION BY DAY;'\
  http://localhost:9000/exec
for filename in docker-compose/*.json; do
  curl -X DELETE "http://localhost:8083/connectors/`basename ${filename} .json`"
  curl -X POST -H "Accept:application/json" -H "Content-Type:application/json" --data "@${filename}" http://localhost:8083/connectors
done
