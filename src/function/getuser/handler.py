import boto3
import json


dynamo = boto3.resource("dynamodb")
table = dynamo.Table('userinformation')


def handler(event, context):
    #print("Context Here", context)
    #print("Event Here", event)

    id = event['pathParameters']['id']
    person_info = get_schema_information_from_db(id)
        
    if (person_info is None):
        response = response_msg(False, json.dumps("Requested id not found in DB, Please check the id and try again!!"))
    else:
        response = response_msg(True, json.dumps(person_info))

    return response


def get_schema_information_from_db(id):
    person_info = None
    person_info = table.get_item(Key={'id': id})
    #print("PERSONINFO", person_info)
    if ('Item' not in person_info):
        return None
    else:
        return person_info['Item']

def response_msg(value, body):
    if value == True:
        response = {'statusCode': 200, 'headers': {'Content-Type': 'application/json'}, 'body': body}
    else:
        response = {'statusCode': 400, 'headers': {'Content-Type': 'application/json'}, 'body': body}
    return response
