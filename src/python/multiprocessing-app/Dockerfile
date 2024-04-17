FROM python:3.10.14-slim-bookworm

WORKDIR /opt/app

COPY src.python.sqs-consumer/sqs_consumer.pex /opt/app/sqs_consumer.pex

ENTRYPOINT ["/bin/bash", "-c", "/opt/app/sqs_consumer.pex"]
