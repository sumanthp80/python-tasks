# Generating dynamic inventory file
# ansible-playbook -i dynamic_inventory.py playbook.yml
#i.e. ansible-playbook -i ansible1.py playbook.yml

import boto3
import json

def get_instances_by_tag(tag_key, tag_value):
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instances(
        Filters=[
            {'Name': 'tag:' + tag_key, 'Values': [tag_value]}
        ]
    )

    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append(instance['PrivateIpAddress'])

    return instances

def generate_inventory():
    inventory = {
        'all': {
            'hosts': get_instances_by_tag('mytagkey', 'mytagvalue'),
            'vars': {
                # Define variables if needed
            }
        },
        '_meta': {
            'hostvars': {}
        }
    }

    print(json.dumps(inventory))

generate_inventory()
