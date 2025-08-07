import json
import boto3



def lambda_handler(event, context, client=None, tableName = 'cloudresumecounter'):
    try:
        if client is None:
            client = boto3.client('dynamodb', region_name="us-east-1")
        print(event)
        body = {}
        statusCode = 200
        headers = {
            "Content-Type": "application/json"
        }
        print(client.get_item(TableName=tableName, Key={'id': {"N":"0"}}))
        if "Item" not in client.get_item(TableName=tableName, Key={'id': {"N":"0"}}).keys():
            client.put_item(
                TableName=tableName,
                Item={
                    'id': {"N": "0"},
                    'count': {"N": "0"}
                }
            )

        if event['routeKey'] == "GET /":
            body = client.get_item(TableName=tableName, Key={'id': {"N":"0"}})
            body = body["Item"]
            count = int(body['count']['N'])+1
            client.update_item(
                TableName=tableName,
                Key={'id': {"N": "0"}},
                AttributeUpdates={
                    'count': {
                        'Value': {"N": str(count)},
                        'Action': 'PUT'
                    }
                }
            )
            body = {"count":str(count)}
    except Exception as e:
        statusCode = 400
        body = str(e)
    body = json.dumps(body)
    res = {
        "statusCode": statusCode,
        "headers": headers,
        "body": body
    }
    return res
