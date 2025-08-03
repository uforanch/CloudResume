import json

from six import assertCountEqual

from application.main import lambda_handler, dynamodb
from unittest.mock import patch, Mock
import boto3
import moto
import unittest


class TestLambdaHandler(unittest.TestCase):
    @moto.mock_aws
    def test_lambda_handler_emptydb(self):
        #dynamodb = boto3.client("dynamodb", region_name="us-east-1")
        dynamodb = boto3.resource("dynamodb")
        dynamodb.create_table(TableName='clouresumecounter',
                           AttributeDefinitions=[{"AttributeName":"id", "AttributeType":"N"}],
                           KeySchema=[{"AttributeName":"id", "KeyType":"HASH"}],
                           BillingMode='PAY_PER_REQUEST')
        table = dynamodb.Table('clouresumecounter')
        event = {
            "routeKey": "GET /"
        }
        context = {}


        response = lambda_handler(event, context, table=table)

        self.assertIsInstance(response, dict)
        self.assertIn("statusCode", response)
        self.assertIn("body", response)
        response_body = json.loads(response["body"])
        assert response_body["count"]=="1"

        response = lambda_handler(event, context, table=table)

        self.assertIsInstance(response, dict)
        self.assertIn("statusCode", response)
        self.assertIn("body", response)
        response_body = json.loads(response["body"])
        assert response_body["count"]=="2"
        #print(table.mock_calls)
