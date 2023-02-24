import boto3
s3 = boto3.client('s3')

response = s3.select_object_content(
    Bucket='botobucket69',
    Key='files/employees.csv',
    Expression='Select s.name s.email from S3Object s',
    ExpressionType='SQL',
    InputSerialization={
        'CSV': {'FileHeaderInfo': 'Use'}},
    OutputSerialization={'CSV': {}}
)

for event in response['Payload']:
    if 'Records' in event:
         print(event['Records']['Payload'].decode())
