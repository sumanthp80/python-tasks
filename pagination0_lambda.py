import boto3

def stop_instances(instance_ids):
    ec2 = boto3.client('ec2')
    try:
        response = ec2.stop_instances(InstanceIds=instance_ids)
        return response
    except ec2.exceptions.ClientError as e:
        print(f"Error occurred while stopping instances: {e.response['Error']['Message']}")
        return None

def start_instances(instance_ids):
    ec2 = boto3.client('ec2')
    try:
        response = ec2.start_instances(InstanceIds=instance_ids)
        return response
    except ec2.exceptions.ClientError as e:
        print(f"Error occurred while starting instances: {e.response['Error']['Message']}")
        return None

def handle_instances(action):
    ec2 = boto3.client('ec2')
    filters = [
        {'Name': 'tag:Environment', 'Values': ['dev']}
    ]

    if action == 'stop':
        filters.append({'Name': 'instance-state-name', 'Values': ['running']})
    elif action == 'start':
        filters.append({'Name': 'instance-state-name', 'Values': ['stopped']})

    paginator = ec2.get_paginator('describe_instances')
    response_iterator = paginator.paginate(Filters=filters)

    instance_ids = []
    for page in response_iterator:
        for reservation in page['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                instance_ids.append(instance_id)

    if len(instance_ids) != 0:
        if action == 'stop':
            response = stop_instances(instance_ids)
            if response is not None:
                print(response)
        elif action == 'start':
            response = start_instances(instance_ids)
            if response is not None:
                print(response)
    else:
        if action == 'stop':
            print("There are currently no running instances with the tag 'Environment=dev'.")
        elif action == 'start':
            print("There are currently no stopped instances with the tag 'Environment=dev'.")

def lambda_handler(event, context):
    try:
        handle_instances(event['action'])
        # handle_instances('start')

    except Exception as e:
        print(f"An error occurred: {e}")

    # Return a response if required
    return {
        'statusCode': 200,
        'body': 'Lambda execution completed successfully'
    }

# Uncomment the line below to execute the code outside of Lambda
# handle_instances('stop')
handle_instances('start')
