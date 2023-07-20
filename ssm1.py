import boto3

# SSM Automation document details
automation_document_name = 'YOUR_AUTOMATION_DOCUMENT_NAME'
parameter_name = 'YOUR_PARAMETER_NAME'

# Connect to AWS services
ssm_client = boto3.client('ssm')

def lambda_handler(event, context):
    response = ssm_client.start_automation_execution(
        DocumentName=automation_document_name,
        DocumentVersion='$LATEST',
        Parameters={
            'ParameterName': [parameter_name]
        }
    )

    execution_id = response['AutomationExecutionId']
    print(f"SSM Automation execution started with execution ID: {execution_id}")
