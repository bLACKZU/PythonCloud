import boto3

ec2 = boto3.resource('ec2')
client = boto3.client('sns')
backup_filter = [
        {
            'Name': 'tag:Backup',
            'Values': [
                'Yes',
            ]    
        }
]     
snapshot_ids=[]      
for instance in ec2.instances.filter(Filters=backup_filter):
    for vol in instance.volumes.all():
        snapshot=vol.create_snapshot(Description="Created by Boto3")
        snapshot_ids.append(snapshot.snapshot_id)
response = client.publish(TopicArn='arn:aws:sns:us-east-1:781666521876:snapshots', Subject="Ebs snapshots", Message=str(snapshot_ids))

        
