import boto3

ec2 = boto3.resource('ec2')
print(type(ec2.instances))
for i in ec2.instances.all():
    print(i)
# list = ec2.instances.filter(Filters=[
#         {
#             'Name': 'instance-state-name',
#             'Values': [
#                 'running',
#             ]    
#         }       
#         ])
   