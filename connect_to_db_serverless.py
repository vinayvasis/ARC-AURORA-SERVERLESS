import os
import os.path
import sys
import botocore
import boto3
import json
from .constants import cluster_arn, secret_arn



# Use latest boto3 from local environment
# LAMBDA_TASK_ROOT = os.environ["LAMBDA_TASK_ROOT"]
# sys.path.insert(0, LAMBDA_TASK_ROOT+"/boto3")


def call_rds_data_api(template_name):
    rds_data = boto3.client('rds-data')

    sql = """
          INSERT INTO TEMPLATE(template_name)
          VALUES( :template_name)
          """
    param1 = {'name': 'template_name', 'value': {'stringValue': template_name}}
    param_set = [param1]

    response = rds_data.execute_statement(
        resourceArn=cluster_arn,
        secretArn=secret_arn,
        database='tutorial',
        sql=sql,
        parameters=param_set)

    print(str(response))


def execute_query(sql_statement):
    rds_data = boto3.client('rds-data')

    response = rds_data.execute_sql(
        awsSecretStoreArn='string',
        database='string',
        dbClusterOrInstanceArn='string',
        schema='string',
        sqlStatements=sql_statement
    )
    print(str(response))


def get_api(event):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps(event, indent=4),
    }


def lambda_handler(event, context):
    # call from api gateway

    # json_body = json.dumps(event, indent=4)
    # print(json_body)

    # sample json print

    with open("sample.json") as json_file:
        json_data = json.load(json_file)
        print(json_data)

    # fill template_name here
    template_name = ""
    call_rds_data_api(template_name)

# lambda_handler(None,None)
