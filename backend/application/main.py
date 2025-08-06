import json
import boto3

client = boto3.client('dynamodb')
dynamodb = boto3.resource("dynamodb")
tableName = 'cloudresumecounter'
dynamo_table = dynamodb.Table(tableName)


def lambda_handler(event, context, table=None):
    try:
        if table is None:
            table = dynamo_table
        print(event)
        body = {}
        statusCode = 200
        headers = {
            "Content-Type": "application/json"
        }

        if "Item" not in table.get_item(Key={'id': 0}).keys():
            table.put_item(
                Item={
                    'id': 0,
                    'count': 0
                })


        if event['routeKey'] == "GET /":
            body = table.get_item(
                Key={'id': 0})
            body = body["Item"]
            responseBody = [{'id': body['id'], 'count': body['count']+1}]
            table.update_item(Key={'id':0}, AttributeUpdates={'count':{"Value":body['count']+1,"Action":"PUT"}})
            body = {"count":str(body['count']+1)}
    except Exception as e:
        statusCode = 400

        body = str(e)
    body = json.dumps(body)
    res = {
        "statusCode": statusCode,
        "headers": headers,
        "body": body
    }
    print(res)
    return res
