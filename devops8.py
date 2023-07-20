'''
AWS Lambda Function Scheduled Invocation:
This script demonstrates how to schedule the invocation of an AWS Lambda function using Boto3. 
It allows you to configure a CloudWatch Events rule to trigger the Lambda function at specific intervals.
'''

import boto3

# Create a CloudWatch Events client
events_client = boto3.client('events')

# Create a rule to schedule Lambda function invocation
rule_name = 'my-lambda-schedule-rule'
lambda_function_arn = 'arn:aws:lambda:us-east-1:553999167352:function:my-lambda-function'
cron_expression = '0 12 * * ? *'  # Every day at 12 PM (UTC)
response = events_client.put_rule(
    Name=rule_name,
    ScheduleExpression=cron_expression,
    State='ENABLED'
)

# Add a target to the rule to invoke the Lambda function
target_id = 'my-lambda-target'
events_client.put_targets(
    Rule=rule_name,
    Targets=[
        {
            'Id': target_id,
            'Arn': lambda_function_arn
        }
    ]
)
