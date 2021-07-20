import os
import os.path
import sys

# Use latest boto3 from local environment
#LAMBDA_TASK_ROOT = os.environ["LAMBDA_TASK_ROOT"]
#sys.path.insert(0, LAMBDA_TASK_ROOT+"/boto3")

# Required imports
import botocore
import boto3

# Imports for your app
from datetime import datetime

# Update your cluster and secret ARNs
cluster_arn = 'arn:aws:rds:us-east-1:0000000000:cluster:my-cluster' 
secret_arn = 'arn:aws:secretsmanager:us-east-1:0000000000:secret:my-secret'

def lambda_handler(event, context):
    if 'Records' not in event or 'Sns' not in event['Records'][0]:
        print('Not an SNS event!')
        print(str(event))
        return

    for record in event['Records']:
        call_rds_data_api(record['Sns']['Timestamp'], record['Sns']['Message'])


def call_rds_data_api(timestamp, message):
    rds_data = boto3.client('rds-data')

    sql = """
          INSERT INTO sample_table(received_at, message)
          VALUES(TO_TIMESTAMP(:time, 'YYYY-MM-DD HH24:MI:SS'), :message)
          """

    param1 = {'name':'time', 'value':{'stringValue': timestamp}}
    param2 = {'name':'message', 'value':{'stringValue': message}}
    param_set = [param1, param2]
 
    response = rds_data.execute_statement(
        resourceArn = cluster_arn, 
        secretArn = secret_arn, 
        database = 'tutorial', 
        sql = sql,
        parameters = param_set)
    
    print(str(response));