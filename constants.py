# move ARN's and other variable constants here

# Update your cluster and secret ARNs
cluster_arn = 'arn:aws:rds:us-east-1:0000000000:cluster:my-cluster'
secret_arn = 'arn:aws:secretsmanager:us-east-1:0000000000:secret:my-secret'

template_select_query = """SELECT * from TEMPLATE"""
print(template_select_query)

template_insert_query = """INSERT INTO TEMPLATE (template_name) VALUES (%s)"""
print(template_insert_query % ("Financial"))
