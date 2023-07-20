'''
Get Cluster Logs from EKS:
This script demonstrates how to retrieve the logs of a specific container running in an EKS cluster. 
It can be used for troubleshooting container issues or analyzing logs.
'''

import boto3

# Create an EKS client
eks = boto3.client('eks')

# Specify the cluster details
cluster_name = 'my-cluster'
namespace = 'default'
pod_name = 'my-pod'
container_name = 'my-container'

# Get logs from a container
response = eks.describe_cluster_logging(
    name=cluster_name
)

# Check if container logs are enabled
if 'clusterLogging' in response and response['clusterLogging']:
    cluster_logging = response['clusterLogging']
    for log_config in cluster_logging:
        if log_config['enabled']:
            log_types = log_config['types']
            if 'container' in log_types:
                # Retrieve container logs
                logs_client = boto3.client('logs')
                log_group_name = '/aws/containerinsights/{cluster_name}/application'.format(cluster_name=cluster_name)
                log_stream_name = '{namespace}/{pod_name}/{container_name}'.format(
                    namespace=namespace,
                    pod_name=pod_name,
                    container_name=container_name
                )
                log_events = logs_client.get_log_events(
                    logGroupName=log_group_name,
                    logStreamName=log_stream_name
                )
                for event in log_events['events']:
                    print(event['message'])
