from application.main import lambda_handler
from unittest.mock import patch, Mock
import boto3
import moto
import unittest


class TestLambdaHandler(unittest.TestCase):
    @moto.mock_aws
    def test_lambda_handler_emptydb(self):
        dyanamodb = boto3.resource("dynamodb", region_name="us-east-1")
        dyanamodb.create_table(TableName='clouresumecounter',
                           AttributeDefinitions=[{"AttributeName":"id", "AttributeType":"N"}],
                           KeySchema=[{"AttributeName":"id", "KeyType":"HASH"}],
                           BillingMode='PAY_PER_REQUEST')
        table = dyanamodb.Table('clouresumecounter')
        event = {
            "routeKey": "GET /"
        }
        context = {}


        response = lambda_handler(event, context, table=table)

        self.assertIsInstance(response, dict)
        self.assertIn("statusCode", response)
        self.assertIn("body", response)
        #print(table.mock_calls)
