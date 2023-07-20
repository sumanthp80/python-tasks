'''
Python Kubernetes Client:
This script demonstrates how to use the official Kubernetes Python client library 
(client-python) to interact with the Kubernetes API. 
It provides a foundation for building CRDs and controllers in Python.
'''

from kubernetes import client, config

# Load Kubernetes configuration
config.load_kube_config()

# Create an instance of the Kubernetes API client
api_client = client.ApiClient()

# Example: List all pods in a namespace
v1 = client.CoreV1Api(api_client)
pod_list = v1.list_namespaced_pod(namespace="default")
for pod in pod_list.items:
    print(pod.metadata.name)
