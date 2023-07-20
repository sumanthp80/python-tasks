import boto3
import csv
from concurrent.futures import ThreadPoolExecutor

# S3 bucket details
s3_bucket_name = 'terraform-sumanth21'
s3_prefix = 'path/to/files/'  # Optional: Prefix to add to S3 object keys

# CSV file details
csv_file_path = 'path/to/csv/file.csv'  # Replace with the path to your CSV file
filename_column_name = 'filename'  # Replace with the column name that contains the filenames

# # Retrieve AWS credentials from AWS Secrets Manager
# secrets_manager_client = boto3.client('secretsmanager', region_name='us-west-2')  # Replace with your desired AWS region
# secrets_response = secrets_manager_client.get_secret_value(SecretId='YOUR_SECRET_ID')
# secrets = secrets_response['SecretString']
# credentials = json.loads(secrets)

# Connect to S3 using retrieved credentials
s3_client = boto3.client(
    's3',
    # aws_access_key_id=credentials['aws_access_key_id'],
    # aws_secret_access_key=credentials['aws_secret_access_key'],
    region_name='us-east-1'  # Replace with your desired AWS region
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
