import boto3
s3 = boto3.client('s3')
response = s3.create_bucket(
    ACL='private',
    Bucket='botobucket69',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-1'
    }
)
    