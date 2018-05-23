import json

def handler(event, context):
    response = {'statusCode': 400, 'headers': {'Content-Type': 'application/json'}, 'body': json.dumps("Requested source does not exist!! Please verfify the URL, Path-Parameter and Methodprovided!!")
}
    return response

