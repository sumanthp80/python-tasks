'''
This script demonstrates how to publish a message to an AWS SNS topic using Boto3. 
It allows you to send notifications or broadcast messages to subscribers of the SNS topic.
'''

import boto3

# Create an SNS client
sns = boto3.client('sns')

# Publish a message to an SNS topic
topic_arn = 'arn:aws:sns:us-east-1:553999167352:my-topic'
message = 'Hello, world!'
response = sns.publish(TopicArn=topic_arn, Message=message)

# Print the message ID
print('Message ID:', response['MessageId'])
