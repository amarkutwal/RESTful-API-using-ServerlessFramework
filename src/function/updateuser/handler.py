import json, boto3

dynamo = boto3.resource("dynamodb")
table = dynamo.Table('userinformation')


def handler(event, context=None):
    #print("Evnt Here", event)
    id, field_name, field_value = parse_the_input(event)
    response = modify_field(id, field_name, field_value)
    return response


def parse_the_input(event):
    #print("getfile handler event:", event)

    # Validate inputs
    path_params = event["pathParameters"]
    if "id" not in path_params:
        return response_msg(False, json.dumps("URL path-param 'id' not specified."))

    id = path_params["id"]
    #print("Event body here", event['body'])
    body = json.loads(event['body'])
    fields = body['fields']
    #print("body fields", fields)
    for key, value in fields.items():
        field_name = key
       #print("Field_NAME here", field_name)
        field_value = value
    return id, field_name, field_value

def modify_field(id, field_name, field_value):
    item = get_row_from_files_table(id)
    #print("Item from get", item)
    if item is None:
        return response_msg(False, json.dumps("Invalid ID specified, please check the id and try again!"))

    #print("Item from dynamodb", item)
    #item = convert_dynamo_file_row_to_json(item)
    #print("field_name here", field_name)
    if field_name not in item:
        return response_msg(False, json.dumps("Invalid field specified, please check the field and try again!"))
    
    item[field_name] = field_value
    update_metadata(item)
    # All the inputs are valid
    response = get_row_from_files_table(id)
    #print("response from code to convert dynamodb function", response)

    return response_msg(True, json.dumps(response))


def get_row_from_files_table(id):
    get_response = None
    get_response = table.get_item(Key={'id': id})
    #print("get_response from table", get_response)
    if ('Item' not in get_response):
        return None
    else:
        return get_response['Item']


def update_metadata(doc_metadata):
    #print(doc_metadata)
    if (table):
        table.put_item(Item=doc_metadata)
    #print("put response",response)
    
def response_msg(value, body):
    if value == True:
        response = {'statusCode': 200, 'headers': {'Content-Type': 'application/json'}, 'body': body}
    else:
        response = {'statusCode': 400, 'headers': {'Content-Type': 'application/json'}, 'body': body}
    return response
