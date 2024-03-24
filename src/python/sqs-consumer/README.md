```
$ aws configure --profile localstack
```

```
AWS Access Key ID [None]: dummy
AWS Secret Access Key [None]: dummy
Default region name [None]: ap-northeast-1
Default output format [None]: json

```

```
export QUEUE_URL=http://sqs.ap-northeast-1.localhost.localstack.cloud:4566/000000000000/test-queue
```

```
aws sqs send-message --queue-url ${QUEUE_URL} --message-body "Test1" --region ap-northeast-1
```


```
GIT_COMMIT=test pants package :
docker run --rm \
  --net=host \
  -e AWS_ACCESS_KEY_ID=dummy \
  -e AWS_SECRET_ACCESS_KEY=dummy \
  -e AWS_DEFAULT_REGION=ap-northeast-1 \
  -e AWS_REGION=ap-northeast-1 \
  -e AWS_ENDPOINT_URL=http://localhost:4566 \
  -t sqs_consumer:test
```

