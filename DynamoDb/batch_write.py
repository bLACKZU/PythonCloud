import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')

with table.batch_writer() as batch:
    for i in range(10):
        batch.put_item(Item={
            'emp_id' : i,
            'name' : 'name{}'.format(i)
        })