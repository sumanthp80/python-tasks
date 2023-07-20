
'''
S3 Bucket Operations:
This script demonstrates how to interact with S3 buckets using Boto3. 
It allows you to 
create, list, upload, download, and delete objects in S3 buckets.
'''
import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Create an S3 bucket
bucket_name = 'sumanth-terraform22'
s3.create_bucket(Bucket=bucket_name)

# List objects in the bucket
response = s3.list_objects_v2(Bucket=bucket_name)
if 'Contents' in response:
    for obj in response['Contents']:
        print('Object:', obj['Key'])

# Upload a file to the bucket
#file_path = 'path/to/file.txt'
file_path = './file.txt'
object_key = 'file.txt'
s3.upload_file(file_path, bucket_name, object_key)

# Download a file from the bucket
download_path = './download.txt'
s3.download_file(bucket_name, object_key, download_path)

# Delete the object from the bucket
s3.delete_object(Bucket=bucket_name, Key=object_key)

# Delete the bucket
s3.delete_bucket(Bucket=bucket_name)
