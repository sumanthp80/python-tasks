'''
AWS Lambda Function Deployment:
This script demonstrates how to deploy an AWS Lambda function using Boto3. 
It allows you to create or update a Lambda function, 
specify the function code, and set the required permissions.
'''
import boto3
import zipfile

# Create a Lambda client
lambda_client = boto3.client('lambda')

# Specify the function details
function_name = 'my-function'
handler = 'lambda_function.lambda_handler'
runtime = 'python3.8'

# Create a ZIP file with the function code
zip_filename = 'function_code.zip'
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    zipf.write('lambda_function.py')

# Create or update the Lambda function
with open(zip_filename, 'rb') as zipfile:
    lambda_client.create_function(
        FunctionName=function_name,
        Handler=handler,
        Runtime=runtime,
        Role='arn:aws:iam::123456789012:role/my-role',
        Code={'ZipFile': zipfile.read()},
        Publish=True
    )

# Clean up the ZIP file
import os
os.remove(zip_filename)
