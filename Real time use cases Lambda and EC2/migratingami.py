import boto3

#Create image id of instance

source_region = 'us-east-1'
ec2 = boto3.resource('ec2', region_name=source_region)
instances = ec2.instances.filter(InstanceIds=['i-074303992951e815d'])
image_ids=[]
for instance in instances:
    image = instance.create_image(Name="Demo-Boto - " + instance.id, Description="Demo-Boto" + instance.id)
    image_ids.append(image.id)
print("Images to be copied {}".format(image_ids))


#Get waiter for image_available

client = boto3.client('ec2', region_name=source_region)
waiter = client.get_waiter('image_available')
 
waiter.wait(Filters=[{'Name': 'image_id', 'Values': image_ids
}])

#Copy images to destination region

destination_region = 'us-east-2'
client = boto3.client('ec2', region_name=destination_region)
for image_id in image_ids:
    client.copy_image(Name='Boto3 copy '+ image_id,
    SourceImageId=image_id,
    SourceRegion=source_region)