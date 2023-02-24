import boto3

#Create a list of unused volumes
ec2_client = boto3.client('ec2')
volumes = ec2_client.describe_volumes()

unused_volumes = []

for volume in volumes['Volumes']:
    if len(volume['Attachments']) == 0:
        unused_volumes.append(volume['VolumeId'])

email_body = "### UNUSED VOLUMES ### \n"

for vol in unused_volumes:
    email_body = email_body + "VolumeId = {}".format(vol)



#Create SNS topic and subscription
sns_client = boto3.client('sns')
topic = sns_client.create_topic(Name='topic_volume')

topicARN = topic['TopicArn']
endpoint = 'satyakighosh65@gmail.com'
sns_client.subscribe(TopicArn = topicARN, Protocol = 'email', Endpoint = endpoint)

#Send email about unused volumes
sns_client.publish(TopicArn = topicARN, Subject = "Unused Volumes", Message = email_body)
