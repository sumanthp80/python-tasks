'''
AWS CloudWatch Logs Analysis:
This script utilizes the Boto3 library to retrieve and analyze log data from AWS CloudWatch Logs. 
It allows you to fetch log events, 
filter them based on criteria, and perform analysis or reporting tasks.
'''

import boto3
from datetime import datetime

# Create a CloudWatch Logs client
logs_client = boto3.client('logs')

# Get log events from a log group and log stream
log_group_name = '/aws/lambda/s3report'
#log_stream_name = '2023/07/11'
log_stream_name = '2023/07/11/[$LATEST]c9188e0bb33e4a8cadaac9481caf6a44'

response = logs_client.get_log_events(
    logGroupName=log_group_name,
    logStreamName=log_stream_name
)

# Process log events
for event in response['events']:
    timestamp_epoch1_milli = event['timestamp']
    timestamp_epoch1 = timestamp_epoch1_milli / 1000
    print('timestamp_epoch1: ',timestamp_epoch1)
    timestamp = datetime.fromtimestamp(timestamp_epoch1)
    message = event['message']
    # Perform analysis or reporting tasks
    # ...
    print(timestamp)
    print(message)

# Paginate through log events if more than 10000 events
while 'nextToken' in response:
    next_token = response['nextToken']
    response = logs_client.get_log_events(
        logGroupName=log_group_name,
        logStreamName=log_stream_name,
        nextToken=next_token
    )
    # Process log events
    # ...
