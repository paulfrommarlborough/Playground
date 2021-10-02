import boto3
from pprint import pprint
from botocore.exceptions import ClientError

dynamodb=None
table=None
systemname=None
systemtype=None

# table systemdata
#   value = systemname
#
print('dynamo db test...')

if not dynamodb:
    dynamodb = boto3.resource('dynamodb', region_name="us-east-1")

    #        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

table = dynamodb.Table('systemdata')

print(table)

try:
    response = table.get_item(Key={'SystemName': systemname, 'SystemType': systemtype})

except ClientError as e:
    print(e.response['Error']['Message'])
else:
    pprint( response['Item']  )