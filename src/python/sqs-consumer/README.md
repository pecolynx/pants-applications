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