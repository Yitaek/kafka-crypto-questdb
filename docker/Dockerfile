FROM alpine:latest AS builder

RUN wget https://github.com/questdb/kafka-questdb-connector/releases/download/v0.3/kafka-questdb-connector-0.3-bin.zip && \
    unzip kafka-questdb-connector-*-bin.zip
    
FROM confluentinc/cp-kafka-connect:7.3.0
COPY --from=builder /kafka-questdb-connector/*.jar /usr/share/java/kafka/