
'''
AWS CloudFormation Stack Update:
This script demonstrates how to update an existing CloudFormation stack programmatically using Boto3. 
It allows you to modify the stack's template, parameters, or other properties and perform a stack update.

'''
import boto3

# Create a CloudFormation client
cloudformation = boto3.client('cloudformation')

# Specify the stack details for update
stack_name = 'my-stack'
template_url = 'https://s3.amazonaws.com/my-bucket/updated-template.yml'
parameters = [
    {'ParameterKey': 'Param1', 'ParameterValue': 'NewValue1'},
    {'ParameterKey': 'Param2', 'ParameterValue': 'NewValue2'}
]

# Update the CloudFormation stack
response = cloudformation.update_stack(
    StackName=stack_name,
    TemplateURL=template_url,
    Parameters=parameters,
    Capabilities=['CAPABILITY_IAM']
)

# Wait for the stack update to complete
cloudformation.get_waiter('stack_update_complete').wait(StackName=stack_name)
