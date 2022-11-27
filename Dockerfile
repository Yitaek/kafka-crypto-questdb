FROM confluentinc/cp-kafka-connect-base:6.1.0

RUN confluent-hub install --no-prompt confluentinc/kafka-connect-jdbc:10.0.1