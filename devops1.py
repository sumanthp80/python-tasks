'''
This script uses the Boto3 library to provision EC2 instances programmatically. 
It allows you to specify instance type, security groups, key pairs, and other configurations.
'''

import boto3
from botocore.exceptions import ClientError

# Create an EC2 client
ec2 = boto3.client('ec2')

# Specify the instance details
instance_details = {
    'ImageId': 'ami-06ca3ca175f37dd66',
    'InstanceType': 't2.micro',
    'KeyName': 'May29',
    'SecurityGroupIds': ['sg-0ed4e4d2a43d7bcb9'],
    'MinCount': 1,
    'MaxCount': 1
}

# Launch the EC2 instance(s)
response = ec2.run_instances(**instance_details)

#print(instances)
print(ec2.waiter_names)
instances=[]

# Print instance IDs
for instance in response['Instances']:
    print('Created instance:', instance['InstanceId'])
    holdon1 = ec2.get_waiter('instance_running')
    holdon1.wait(InstanceIds=[instance['InstanceId']])
    print('Created instance is running now:', instance['InstanceId'])
    instances.append(instance['InstanceId'])

for instance in response['Instances']:
    ec2.terminate_instances(InstanceIds=instances)
    