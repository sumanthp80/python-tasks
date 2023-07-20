'''
Scale EKS Cluster Node Group:
This script demonstrates how to scale the worker nodes in an EKS cluster. 
It allows you to increase or decrease the desired number of worker nodes in a node group.
'''

import boto3

# Create an EKS client
eks = boto3.client('eks')

# Specify the cluster and node group details
cluster_name = 'my-cluster'
nodegroup_name = 'my-nodegroup'
desired_capacity = 5  # The desired number of worker nodes

# Scale the node group
eks.update_nodegroup_config(
    clusterName=cluster_name,
    nodegroupName=nodegroup_name,
    scalingConfig={
        'desiredSize': desired_capacity
    }
)
