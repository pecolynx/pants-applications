import boto3


kinesis = boto3.client('kinesis')

kinesis.put_record(Data='bytes', PartitionKey='string', StreamName='sample-stream')
