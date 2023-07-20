'''
List Pods in EKS Cluster:
This script uses the boto3 library to list all pods in an EKS cluster. 
It can be helpful for troubleshooting and verifying the status of pods.
'''

import boto3

# Create an EKS client
eks = boto3.client('eks')

# Specify the cluster details
cluster_name = 'my-cluster'

# List pods in the cluster
response = eks.list_pod_executions(
    clusterName=cluster_name
)

# Print pod details
pods = response['podExecutions']
for pod in pods:
    print('Pod Name:', pod['pod'])
    print('Pod Status:', pod['status'])
    print('---')
