import json
import boto3

client = boto3.client('dynamodb')
dynamodb = boto3.resource("dynamodb")
tableName = 'clouresumecounter'
dynamo_table = dynamodb.Table(tableName)


def lambda_handler(event, context, table=None):
    if table is None:
        table = dynamo_table
    print(event)
    body = {}
    statusCode = 200
    headers = {
        "Content-Type": "application/json"
    }

    try:
        table.get_item(
            Key={'id': 0})
    except KeyError:
        table.put_item(
            Item={
                'id': 0,
                'count': 0
            })

    try:
        if event['routeKey'] == "GET /":
            body = table.get_item(
                Key={'id': 0})
            body = body["Item"]
            responseBody = [
                {'id': body['id'], 'count': body['count']+1}]
            table.update_item(Key={'id':0}, AttributeUpdates={'count':{"Value":body['count']+1,"Action":"PUT"}})
            body = responseBody
    except KeyError:
        statusCode = 400
        body = 'Unsupported route: ' + event['routeKey']
    body = json.dumps(body)
    res = {
        "statusCode": statusCode,
        "headers": headers,
        "body": event
    }
    print(res)
    return res
