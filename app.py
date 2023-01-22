import boto3
import json

# define the DynamoDB table that Lambda will connect to
tableName = "visitor"

# create the DynamoDB resource
dynamo = boto3.resource('dynamodb').Table(tableName)

print('Loading function')

def lambda_handler(event, context):
    def ddb_read(x):
        dynamo.get_item(**x)

    def ddb_update(x):
        dynamo.update_item(**x)
        
    def echo(x):
        return x

    operation = event['operation']

    operations = {
        'read': ddb_read,
        'update': ddb_update,
        'echo': echo,
    }

    if operation in operations:
        return operations[operation](event.get('payload'))
    else:
        raise ValueError('Unrecognized operation "{}"'.format(operation))