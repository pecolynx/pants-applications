#!/bin/bash
# awslocal s3 mb s3://test-bucket
# cd /home/localstack/data/
# awslocal s3 cp sample.txt s3://test-bucket/
# awslocal s3 ls s3://test-bucket

awslocal kinesis create-stream \
  --stream-name sample-stream \
  --shard-count 1 \
  --region ap-northeast-1

awslocal dynamodb create-table \
  --table-name sample-applicaiton \
  --key-schema AttributeName=leaseKey,KeyType=HASH \
  --attribute-definitions AttributeName=leaseKey,AttributeType=S \
  --billing-mode PAY_PER_REQUEST \
  --region ap-northeast-1
