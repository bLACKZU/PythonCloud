import boto3
from datetime import timedelta, timezone, datetime

ec2 = boto3.resource('ec2')

snapshots = ec2.snapshots.filter(OwnerIds=['self'])

for snapshot in snapshots:
    start_time = snapshot.start_time
    delete_time = datetime.now(tz=timezone.utc) - timedelta(days = 15)
    if delete_time > start_time:
        snapshot.delete()
        print("Snapshot with id = {} deleted".format(snapshot.snapshot_id))