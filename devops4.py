'''
AWS CloudFormation Stack Provisioning:
This script uses the Boto3 library to provision AWS CloudFormation stacks programmatically. 
It allows you to create, update, and delete CloudFormation stacks.
'''

import boto3

# Create a CloudFormation client
cloudformation = boto3.client('cloudformation')

# Specify the stack details
stack_name = 'my-stack'
template_url = 'https://s3.amazonaws.com/my-bucket/my-template.yml'
parameters = [
    {'ParameterKey': 'Param1', 'ParameterValue': 'Value1'},
    {'ParameterKey': 'Param2', 'ParameterValue': 'Value2'}
]

# Create or update the CloudFormation stack
response = cloudformation.create_or_update_stack(
    StackName=stack_name,
    TemplateURL=template_url,
    Parameters=parameters,
    Capabilities=['CAPABILITY_IAM']
)

# Wait for the stack to complete
cloudformation.get_waiter('stack_create_complete').wait(StackName=stack_name)

# Print stack outputs
response = cloudformation.describe_stacks(StackName=stack_name)
if 'Stacks' in response:
    stack = response['Stacks'][0]
    outputs = stack.get('Outputs', [])
    for output in outputs:
        print('Output:', output['OutputKey'], '=', output['OutputValue'])

# Delete the stack
cloudformation.delete_stack(StackName=stack_name)
