import boto3
s3 = boto3.client('s3')

file_reader = open('D:\Python for Cloud\S3\create_bucket.py').read()
response = s3.put_object(
    ACL='private',
    Body= file_reader,
    Bucket='botobucket69',
    Key = 'create_bucket.py'
    
    )