import boto3

def remove_duplicates(amis):
    unique_ami = []

    for ami in amis:
        if ami not in unique_ami:
            unique_ami.append(ami)       
    return unique_ami
    
ec2_client = boto3.client('ec2')

instances = ec2_client.describe_instances()
used_ami = []

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        used_ami.append(instance['ImageId'])


unique_amis = remove_duplicates(used_ami)

custom_ami = ec2_client.describe_images(Filters=[
        {
            'Name': 'state',
            'Values': [
                'available',
            ]
        },
    ], Owners=[
        'self',
    ])
custom_ami_list = []
for ami in custom_ami['Images']:
   custom_ami_list.append(ami['ImageId'])

for image in custom_ami_list:
    if image not in unique_amis:
        ec2_client.deregister_image(ImageId=image)

