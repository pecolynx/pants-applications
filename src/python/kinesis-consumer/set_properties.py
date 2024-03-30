# https://github.com/aws-samples/amazon-kinesis-data-processor-aws-fargate/blob/master/consumer/set_properties.py
#
# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
#
# This script sets configuration properties for the KCL

import os

with open("/opt/app/app.properties") as file:
    filedata = file.read()
    filedata = filedata.replace("EXECUTABLE_NAME", os.environ["EXECUTABLE_NAME"])
    filedata = filedata.replace("AWS_REGION", os.environ["AWS_REGION"])
    filedata = filedata.replace("STREAM_ARN", os.environ["STREAM_ARN"])
    filedata = filedata.replace("STREAM_NAME", os.environ["STREAM_NAME"])
    filedata = filedata.replace("APPLICATION_NAME", os.environ["APPLICATION_NAME"])
    filedata = filedata.replace("PROCESSING_LANGUAGE", os.environ["PROCESSING_LANGUAGE"])
    filedata = filedata.replace("SHUTDOWN_GRACE_MILLIS", os.environ["SHUTDOWN_GRACE_MILLIS"])

    if os.getenv("KINESIS_ENDPOINT"):
        filedata = filedata.replace("# kinesisEndpoint", "kinesisEndpoint")
        filedata = filedata.replace("KINESIS_ENDPOINT", os.environ["KINESIS_ENDPOINT"])
    if os.getenv("DYNAMODB_ENDPOINT"):
        filedata = filedata.replace("# dynamoDBEndpoint", "dynamoDBEndpoint")
        filedata = filedata.replace("DYNAMODB_ENDPOINT", os.environ["DYNAMODB_ENDPOINT"])
    if os.getenv("METRICS_LEVEL"):
        filedata = filedata.replace("# metricsLevel", "metricsLevel")
        filedata = filedata.replace("METRICS_LEVEL", os.environ["METRICS_LEVEL"])
    # if os.getenv("retrievalMode = POLLING")
with open("/opt/app/record_processor.properties", "w") as file:
    file.write(filedata)
