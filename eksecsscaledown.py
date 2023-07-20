import boto3

# ECS cluster details
ecs_cluster_name = 'ECS_CLUSTER_NAME'
ecs_service_name = 'ECS_SERVICE_NAME'

# EKS cluster details
eks_cluster_name = 'EKS_CLUSTER_NAME'
eks_nodegroup_name = 'EKS_NODEGROUP_NAME'
desired_capacity = 0  # Set to the desired number of worker nodes during low usage

# Connect to AWS services
ecs_client = boto3.client('ecs')
eks_client = boto3.client('eks')

def lambda_handler(event, context):
    action = event['action']  # Action: 'stop' or 'scale_down'

    if action == 'stop':
        stop_ecs_tasks()
    elif action == 'scale_down':
        scale_down_eks_nodes()

def stop_ecs_tasks():
    try:
        response = ecs_client.update_service(
            cluster=ecs_cluster_name,
            service=ecs_service_name,
            desiredCount=0
        )
        print(f"ECS tasks in cluster {ecs_cluster_name} stopped successfully")
        print(response)
    except Exception as e:
        print(f"Error stopping ECS tasks in cluster {ecs_cluster_name}: {str(e)}")

def scale_down_eks_nodes():
    try:
        response = eks_client.update_nodegroup_config(
            clusterName=eks_cluster_name,
            nodegroupName=eks_nodegroup_name,
            scalingConfig={
                'desiredSize': desired_capacity
            }
        )
        print(f"EKS worker nodes in cluster {eks_cluster_name}/{eks_nodegroup_name} scaled down to {desired_capacity}")
        print(response)
    except Exception as e:
        print(f"Error scaling down EKS worker nodes in cluster {eks_cluster_name}/{eks_nodegroup_name}: {str(e)}")
