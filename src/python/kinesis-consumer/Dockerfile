FROM python:3.11.8-slim-bookworm

ARG LOGBACK_ENCODER="https://repo1.maven.org/maven2/net/logstash/logback/logstash-logback-encoder/7.2/logstash-logback-encoder-7.2.jar"

WORKDIR /opt/app

RUN apt-get update && apt-get install --no-install-recommends -y \
    openjdk-17-jre-headless="17.0.10+7-1~deb12u1" \
    wget="1.21.3-1+b2" \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && wget -q ${LOGBACK_ENCODER}

COPY src/python/kinesis-consumer/requirements.txt /opt/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY src/python/kinesis-consumer/run.sh \
     src/python/kinesis-consumer/app.properties \
     src/python/kinesis-consumer/logback.xml \
     src/python/kinesis-consumer/set_properties.py \
     /opt/app/

COPY src.python.kinesis-consumer/kinesis_consumer.pex /opt/app/kinesis_consumer.pex

CMD ["/bin/sh", "-c", "/opt/app/run.sh"]
