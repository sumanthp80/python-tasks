import boto3
import os

# S3 configuration
s3_bucket = "<S3_BUCKET_NAME>"

def lambda_handler(event, context):
    try:
        # Retrieve the uploaded file details from the Lambda event
        for record in event['Records']:
            s3_event = record['s3']
            bucket_name = s3_event['bucket']['name']
            object_key = s3_event['object']['key']

            # Validate the source bucket (optional)
            if bucket_name != s3_bucket:
                raise ValueError(f"Invalid bucket. Expected: {s3_bucket}, Received: {bucket_name}")

            # Perform additional validation or filtering if needed

            # Get the S3 client
            s3_client = boto3.client('s3')

            # Generate a unique object key for the destination bucket
            dest_object_key = os.path.join("processed", object_key)

            # Copy the object to the destination bucket
            s3_client.copy_object(
                Bucket=s3_bucket,
                Key=dest_object_key,
                CopySource={'Bucket': bucket_name, 'Key': object_key}
            )

            # Delete the original object from the source bucket
            s3_client.delete_object(
                Bucket=bucket_name,
                Key=object_key
            )

            # Perform additional processing tasks on the object as needed
            # ...

        return {
            'statusCode': 200,
            'body': 'Lambda execution completed successfully'
        }
    except ValueError as e:
        print(f"Value error occurred: {e}")
        return {
            'statusCode': 400,
            'body': 'Invalid request'
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        return {
            'statusCode': 500,
            'body': 'Lambda execution encountered an error'
        }
