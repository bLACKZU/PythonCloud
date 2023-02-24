import boto3

client = boto3.client('ec2')
response = client.start_instances(InstanceIds=['i-0a59df56c9f3ce1e6'])
#response = client.stop_instances(InstanceIds=['i-0a59df56c9f3ce1e6'])
#response = client.terminate_instances(InstanceIds=['i-0a59df56c9f3ce1e6'])