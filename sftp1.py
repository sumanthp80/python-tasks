import boto3
import paramiko
import io
#prerequisites
# pip install paramiko boto3
# replace credentials with creds from secret manager
# AWS credentials
#aws_access_key_id = 'YOUR_ACCESS_KEY'
#aws_secret_access_key = 'YOUR_SECRET_KEY'
aws_region = 'us-east-1'  # Replace with your desired AWS region

# SFTP connection details
sftp_host = 'YOUR_SFTP_HOST'
sftp_port = 22
sftp_username = 'YOUR_SFTP_USERNAME'
sftp_password = 'YOUR_SFTP_PASSWORD'

# S3 bucket details
s3_bucket_name = 'terraform-sumanth21'
s3_prefix = 'path/to/files/'  # Optional: Prefix to add to S3 object keys

# Establish SFTP connection
transport = paramiko.Transport((sftp_host, sftp_port))
transport.connect(username=sftp_username, password=sftp_password)
sftp = transport.open_sftp()

# Connect to S3
s3_client = boto3.client(
    's3',
    #aws_access_key_id=aws_access_key_id,
    #aws_secret_access_key=aws_secret_access_key,
    #region_name=aws_region
)

# List files in SFTP directory
sftp_files = sftp.listdir('.')

# Transfer each file to S3
for sftp_file in sftp_files:
    s3_key = s3_prefix + sftp_file
    sftp_file_path = './' + sftp_file
    
    # Read file from SFTP into memory
    file_obj = io.BytesIO()
    sftp.getfo(sftp_file_path, file_obj)
    file_obj.seek(0)  # Reset file object position to start
    
    # Upload file to S3
    s3_client.upload_fileobj(file_obj, s3_bucket_name, s3_key)
    print(f"Uploaded {sftp_file} to S3 bucket {s3_bucket_name} with key {s3_key}")

# Close SFTP connection
sftp.close()
transport.close()
