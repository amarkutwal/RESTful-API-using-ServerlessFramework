import json

def handler(event, context):
    return {'statusCode': 404,
            'headers': {'Content-Type': 'application/json', 'body': json.dumps({'status': '404/405 - bad request', 'error': "Requested source does not exist!! Please verfify the URL, Path-Parameter and Methodprovided!!"})
}

