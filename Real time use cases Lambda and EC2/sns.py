import boto3

sns_client = boto3.client('sns')
topic = sns_client.create_topic(Name='testtopic')

topicARN = topic['TopicArn']
endpoint = 'satyakighosh65@gmail.com'
sns_client.subscribe(TopicArn = topicARN, Protocol = 'email', Endpoint = endpoint)

