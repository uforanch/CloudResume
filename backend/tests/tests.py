import json

from application.main import lambda_handler
from unittest.mock import patch, Mock
import boto3
import moto
import unittest


class TestLambdaHandler(unittest.TestCase):
    @moto.mock_aws
    def test_lambda_handler_emptydb(self):
        client = boto3.client("dynamodb", region_name="us-east-1")
        client.create_table(
            TableName='cloudresumecounter',
            AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "N"}],
            KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
            BillingMode='PAY_PER_REQUEST'
        )
        event = {
            "routeKey": "GET /"
        }
        context = {}


        response = lambda_handler(event, context, client=client)

        self.assertIsInstance(response, dict)
        self.assertIn("statusCode", response)
        self.assertIn("body", response)
        response_body = json.loads(response["body"])

        assert response_body["count"]=="1"

        response = lambda_handler(event, context, client=client)

        self.assertIsInstance(response, dict)
        self.assertIn("statusCode", response)
        self.assertIn("body", response)
        response_body = json.loads(response["body"])

        assert response_body["count"]=="2"

