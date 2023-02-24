import boto3
s3 = boto3.client('s3')
resp = s3.delete_object(Bucket='botobucket69',
    Key='create_bucket.py')
    