'''
Controller Development:
This script demonstrates how to develop a controller in Python
 using the Kubernetes Python client library. 
It allows you to watch and handle events of custom resources in a Kubernetes cluster.
'''

from kubernetes import client, config, watch

# Load Kubernetes configuration
config.load_kube_config()

# Create an instance of the Kubernetes API client
api_client = client.ApiClient()

# Define an event handler for the custom resource
def handle_event(event):
    event_type = event['type']
    custom_resource = event['object']
    custom_resource_name = custom_resource['metadata']['name']
    print(f"Event Type: {event_type}, Custom Resource: {custom_resource_name}")

# Watch events of the custom resource
api = client.CustomObjectsApi(api_client)
resource_version = ""
while True:
    stream = watch.Watch().stream(api.list_cluster_custom_object,
                                  group="mygroup.example.com",
                                  version="v1",
                                  plural="mycrds",
                                  resource_version=resource_version)
    for event in stream:
        handle_event(event)
        resource_version = event['object']['metadata']['resourceVersion']
