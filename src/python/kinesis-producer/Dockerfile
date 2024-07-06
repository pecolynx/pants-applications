FROM python:3.11.8-slim-bookworm

WORKDIR /opt/app

COPY src.python.kinesis-consumer/kinesis_consumer.pex /opt/app/kinesis_consumer.pex

ENTRYPOINT ["/bin/bash", "-c", "/opt/app/kinesis_consumer.pex"]
