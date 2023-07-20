import boto3
import csv
from concurrent.futures import ThreadPoolExecutor

# AWS credentials
aws_access_key_id = 'YOUR_ACCESS_KEY'
aws_secret_access_key = 'YOUR_SECRET_KEY'
aws_region = 'us-west-2'  # Replace with your desired AWS region

# S3 bucket details
s3_bucket_name = 'YOUR_S3_BUCKET_NAME'
s3_prefix = 'path/to/files/'  # Optional: Prefix to add to S3 object keys

# CSV file details
csv_file_path = 'path/to/csv/file.csv'  # Replace with the path to your CSV file
filename_column_name = 'filename'  # Replace with the column name that contains the filenames

# Connect to S3
s3_client = boto3.client(
    's3',
 #   aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)

# Function to upload a single file to S3
def upload_file_to_s3(filename):
    s3_key = s3_prefix + filename
    local_file_path = 'path/to/local/files/' + filename  # Replace with the path to your local files

    # Upload file to S3
    s3_client.upload_file(local_file_path, s3_bucket_name, s3_key)
    print(f"Uploaded {local_file_path} to S3 bucket {s3_bucket_name} with key {s3_key}")

# Read the CSV file
with open(csv_file_path, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    filenames = [row[filename_column_name] for row in reader]

# Upload files to S3 in parallel using multiple threads
with ThreadPoolExecutor() as executor:
    executor.map(upload_file_to_s3, filenames)
