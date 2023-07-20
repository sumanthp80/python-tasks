'''
CRD Definition:
This script demonstrates how to define a Custom Resource Definition (CRD) 
using the Kubernetes Python client library. 
It allows you to specify the API version, kind, and schema of your custom resource.
'''

from kubernetes import client, config

# Load Kubernetes configuration
config.load_kube_config()

# Create a CRD object
crd = client.V1beta1CustomResourceDefinition(
    api_version="apiextensions.k8s.io/v1beta1",
    kind="CustomResourceDefinition",
    metadata=client.V1ObjectMeta(name="my-crd"),
    spec=client.V1beta1CustomResourceDefinitionSpec(
        group="mygroup.example.com",
        version="v1",
        names=client.V1beta1CustomResourceDefinitionNames(
            plural="mycrds",
            singular="mycrd",
            kind="MyCRD",
            short_names=["mc"]
        ),
        scope="Namespaced",
        validation=client.V1beta1CustomResourceValidation(
            open_apiv3_schema=client.V1beta1JSONSchemaProps(
                type="object",
                properties={
                    "spec": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string"
                            }
                        }
                    }
                }
            )
        )
    )
)

# Create the CRD
api_client = client.ApiClient()
api_extensions = client.ApiextensionsV1beta1Api(api_client)
api_extensions.create_custom_resource_definition(body=crd)
