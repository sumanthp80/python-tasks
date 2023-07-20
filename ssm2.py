import boto3

# SSM Parameter Store details
parameter_name = '/my-parameter'

# Connect to AWS services
ssm_client = boto3.client('ssm')

def lambda_handler(event, context):
    try:
        response = ssm_client.get_parameter(
            Name=parameter_name,
            WithDecryption=True
        )
        parameter_value = response['Parameter']['Value']
        print(f"Parameter '{parameter_name}' value: {parameter_value}")
    except Exception as e:
        print(f"Error retrieving parameter '{parameter_name}': {str(e)}")
