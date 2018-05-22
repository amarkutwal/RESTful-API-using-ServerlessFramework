import re
import json, boto3

dynamodb = boto3.resource('dynamodb' , region_name='us-east-1')
table = dynamodb.Table('userinformation')

def lambda_handler(event, context=None):
    response = create_schema(event)
    return response

def validate_require_fields(event):
    try:
        if 'body' in event:
            body = json.loads(event['body'])
        else:
            body = event
        id = body['id']
        fname = body['first_name']
        lname = body['last_name']
        color = body['favourite_colour']
        return True
    except Exception as e:
        return False

def parse_input(event):
    # print(event)
    if 'body' in event:
        body = json.loads(event['body'])
    else:
        body = event

    id = body['id']
    fname = body['first_name']
    lname = body['last_name']
    color = body['favourite_colour']
    return [id, fname, lname, color]

def create_schema(event):
    if(validate_require_fields(event)):
        id, fname, lname, color = parse_input(event)
        if(not does_id_exist(id)):
            insert_new_entry_in_db(id, fname, lname, color)
            return response_msg(True, "New entry added to db!!")
        else:
            return response_msg(False, "Id is not unique!!")
    else:
         return response_msg(False, "Input does not contains require fields, please check the input and try again!!")



def insert_new_entry_in_db(id, fname, lname, color):
    response = table.put_item(Item={
        'id': id,
        'first_name': fname,
        'last_name': lname,
        'favourite_colour': color
    })
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        response = True
    else:
        response = False
    return response


def does_id_exist(id):
    schema_name_from_db = table.get_item(
        Key={
            'id': id
        })
    print(list(schema_name_from_db.keys()))
    if "Item" in list(schema_name_from_db.keys()):
        return True
    else:
        return False


def response_msg(value, body):
    if value == True:
        response = {'statusCode': 200, 'headers': {'Content-Type': 'application/json'}, 'body': body}
    else:
        response = {'statusCode': 400, 'headers': {'Content-Type': 'application/json'}, 'body': body}
    return response

