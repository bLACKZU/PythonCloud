import boto3
s3 = boto3.client('s3')

resp = s3.list_objects(
    Bucket = 'botobucket69'
)

for content in resp['Contents']:
    print(content['Key'])