'''
AWS DynamoDB Table Operations:
This script demonstrates how to interact with AWS DynamoDB tables using Boto3. 
It allows you to create, read, update, and delete items in DynamoDB tables.
'''

import boto3

# Create a DynamoDB client
dynamodb = boto3.client('dynamodb')

# Create a DynamoDB table
table_name = 'my-dynamodb-table'
attribute_definitions = [
    {'AttributeName': 'id', 'AttributeType': 'N'},
    {'AttributeName': 'name', 'AttributeType': 'S'}
]
key_schema = [
    {'AttributeName': 'id', 'KeyType': 'HASH'},
    {'AttributeName': 'name', 'KeyType': 'RANGE'}
]
provisioned_throughput = {
    'ReadCapacityUnits': 1,
    'WriteCapacityUnits': 1
}
dynamodb.create_table(
    TableName=table_name,
    AttributeDefinitions=attribute_definitions,
    KeySchema=key_schema,
    ProvisionedThroughput=provisioned_throughput
)

# Put an item into the table
item = {'id': {'N': '1'}, 'name': {'S': 'John'}}
dynamodb.put_item(TableName=table_name, Item=item)

# Get an item from the table
key = {'id': {'N': '1'}, 'name': {'S': 'John'}}
response = dynamodb.get_item(TableName=table_name, Key=key)
item = response['Item']
print('Item:', item)

# Update an item in the table
item['age'] = {'N': '30'}
dynamodb.put_item(TableName=table_name, Item=item)

# Delete the item from the table
key = {'id': {'N': '1'}, 'name': {'S': 'John'}}
dynamodb.delete_item(TableName=table_name, Key=key)

# Delete the table
dynamodb.delete_table(TableName=table_name)
