build:
	GIT_COMMIT=test pants package :

run:
	docker run --rm \
	--net=host \
	-e AWS_REGION=ap-northeast-1 \
	-e EXECUTABLE_NAME=/opt/app/kinesis_consumer.pex \
	-e STREAM_NAME=sample-stream \
	-e STREAM_ARN=arn:aws:kinesis:ap-northeast-1:000000000000:stream/sample-stream \
	-e APPLICATION_NAME=sample-application \
	-e PROCESSING_LANGUAGE=python/3.11 \
	-e METRICS_LEVEL=None \
	-e SHUTDOWN_GRACE_MILLIS=10000 \
	-e JAVA_LOG_LEVEL=WARN \
	-e KINESIS_ENDPOINT=http://localhost:4566 \
	-e DYNAMODB_ENDPOINT=http://localhost:4566 \
    -e AWS_ACCESS_KEY_ID=access_key_id \
    -e AWS_SECRET_ACCESS_KEY=secret_access_key \
	kinesis_consumer:test

# -e AWS_ENDPOINT=http://localhost:4566 \

# $(eval pid := `ps -ef | grep "MultiLangDaemon" | grep -v "grep" | awk '{print $$$$2}'`)
# kill -s TERM $(pid)
docker-up:
	cd local && docker compose up
stop:
	ps -ef | grep "MultiLangDaemon" | grep -v "grep" | awk '{print $$2}' | sudo xargs kill -15
