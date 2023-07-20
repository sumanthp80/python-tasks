import boto3

# RDS database details
rds_db_instance_identifier = 'RDS_DB_IDENTIFIER'

# Connect to AWS services
rds_client = boto3.client('rds')

def lambda_handler(event, context):
    action = event['action']  # Action: 'start' or 'stop'

    if action == 'start':
        start_rds_database()
    elif action == 'stop':
        stop_rds_database()

def start_rds_database():
    try:
        response = rds_client.start_db_instance(DBInstanceIdentifier=rds_db_instance_identifier)
        print(f"RDS database {rds_db_instance_identifier} started successfully")
        print(response)
    except Exception as e:
        print(f"Error starting RDS database {rds_db_instance_identifier}: {str(e)}")

def stop_rds_database():
    try:
        response = rds_client.stop_db_instance(DBInstanceIdentifier=rds_db_instance_identifier)
        print(f"RDS database {rds_db_instance_identifier} stopped successfully")
        print(response)
    except Exception as e:
        print(f"Error stopping RDS database {rds_db_instance_identifier}: {str(e)}")
