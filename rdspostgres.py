import boto3
import psycopg2
import json

# RDS configuration
rds_host = "<RDS_HOST>"
secret_name = "<SECRET_NAME>"
region_name = "<REGION>"

def get_secret():
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)
    try:
        secret_value = client.get_secret_value(SecretId=secret_name)
        if 'SecretString' in secret_value:
            return secret_value['SecretString']
        else:
            return secret_value['SecretBinary']
    except Exception as e:
        print(f"Error occurred while retrieving secret: {e}")
        raise

def process_data(row):
    # Perform data processing tasks here
    processed_data = {
        'id': row[0],
        'name': row[1],
        'age': row[2]
    }
    return processed_data

def lambda_handler(event, context):
    try:
        # Get database credentials from Secrets Manager
        secret_string = get_secret()
        secret_data = json.loads(secret_string)
        db_username = secret_data.get('username')
        db_password = secret_data.get('password')
        db_name = secret_data.get('dbname')

        if not all([db_username, db_password, db_name]):
            raise ValueError("Missing database credentials in Secrets Manager")

        # Connect to the PostgreSQL instance
        conn = psycopg2.connect(
            host=rds_host,
            user=db_username,
            password=db_password,
            dbname=db_name
        )
        cursor = conn.cursor()

        # Execute SQL query
        query = "SELECT * FROM my_table"
        cursor.execute(query)

        # Fetch results
        results = cursor.fetchall()

        processed_results = []
        for row in results:
            processed_data = process_data(row)
            processed_results.append(processed_data)

        # Close the database connection
        conn.close()

        return {
            'statusCode': 200,
            'body': json.dumps(processed_results)
        }
    except psycopg2.Error as e:
        print(f"Database error occurred: {e}")
        return {
            'statusCode': 500,
            'body': 'Database error'
        }
    except ValueError as e:
        print(f"Value error occurred: {e}")
        return {
            'statusCode': 500,
            'body': 'Value error'
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        return {
            'statusCode': 500,
            'body': 'Lambda execution encountered an error'
        }
