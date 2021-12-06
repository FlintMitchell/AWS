import json
import boto3

region='us-west-2'
ec2 = boto3.client('ec2', region_name=region)

# List all running EC2 instances, regardless of type

def lambda_handler(event, context):

    # TODO implement
    instance_ids = []
    response = ec2.describe_instance_status(
        Filters=[
            {
                'Name': 'instance-state-name', 
                'Values':["running"]
            }
        ]
    )
    
    for instancestatuses in response['InstanceStatuses']:
        instance_ids.append(instancestatuses['InstanceId'])
    
    return instance_ids
