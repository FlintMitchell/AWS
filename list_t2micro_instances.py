import json
import boto3

region='us-west-2'
ec2 = boto3.client('ec2', region_name=region)

# multiple instances
def lambda_handler(event, context):
    # TODO implement
    instance_ids = []

    status = ec2.describe_instances(Filters=[{'Name':'instance-type', 'Values': ["t2.micro"]}])
    instances_full_details = status['Reservations']
    for instance_detail in instances_full_details:
        
        group_instances = instance_detail['Instances']
        print(group_instances)
        for instance in group_instances:
            print(instance)
            instance_id = instance['InstanceId']
            instance_ids.append(instance_id)

    print(instance_ids)
