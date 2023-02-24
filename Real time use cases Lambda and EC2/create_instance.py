
import boto3

# client = boto3.client('s3')
# response = client.list_buckets()

# for b in response['Buckets']:
#     print(b['Name'])


client = boto3.client('ec2')
#response1 = client.create_key_pair(KeyName = 'sdk_key_pair')
response2 = client.run_instances(ImageId='ami-0d67f7df31cd0f0bb', InstanceType='t2.micro', MaxCount=1, MinCount=1)
for instance in response2['Instances']:
    print(instance['InstanceId'])
#print(response1)

