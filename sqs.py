import boto3

def process_records(records):
    # Process each record from the SQS queue
    for record in records:
        # Perform the required processing tasks on the record
        # For example, you can access the record's body and attributes:
        body = record['body']
        message_attributes = record['messageAttributes']
        
        # Process the record as needed
        print(f"Processing record: {body}")
        print(f"Message Attributes: {message_attributes}")
        
        # TODO: Add your processing logic here

def lambda_handler(event, context):
    try:
        # Get the list of records from the SQS event
        records = event['Records']
        
        # Process the records
        process_records(records)

        return {
            'statusCode': 200,
            'body': 'Lambda execution completed successfully'
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        return {
            'statusCode': 500,
            'body': 'Lambda execution encountered an error'
        }
