import boto3
from boto3.dynamodb.conditions import Key

def create_table():
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.create_table(
        TableName='Users',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'N'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1,
        }
    )

    print("Table status:", table.table_status)

def get_item():
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('Users')      
    
    resp = table.get_item(
            Key={
                'id' : 1,
            }
        )
                
    if 'Item' in resp:
        print(resp['Item'])

    #{'id': Decimal('1'), 'email': 'jdoe@test.com', 'last_name': 'Doe', 'first_name': 'Jon'}



def query():
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('Users')      
    
    resp = table.query(
        KeyConditionExpression=Key('id').eq(2)
    )
                
    if 'Items' in resp:
        print(resp['Items'][0])


def create_bunch_of_users():
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('Users') 
    
    for n in range(3):
        table.put_item(Item={
            'id': n,
            'first_name': 'Jon',
            'last_name': 'Doe' + str(n),
            'email': 'jdoe'+ str(n) +'@test.com'
        })


if __name__ == "__main__":    
#    create_table()   
#    create_bunch_of_users()
    query()