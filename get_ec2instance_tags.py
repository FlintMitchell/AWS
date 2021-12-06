import json
import boto3

region='us-west-2'
ec2 = boto3.client('ec2', region_name=region)

# For each instances with the keytag ['user':'Flint Mitchell'], return all of it's tags

def lambda_handler(event, context):
    # TODO implement
    instance_tags = []

    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:user', 
                'Values':['Flint Mitchell']
            }
        ]
    )
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            for tag in instance['Tags']:
                instance_tags.append(tag)
    
    return instance_tags
