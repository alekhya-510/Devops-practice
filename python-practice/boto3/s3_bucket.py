import boto3
client = boto3.client('s3')
response = client.create_bucket(
   
    Bucket='hanvi-demo-bucket',
)
response1 = client.get_bucket_acl(
    Bucket='hanvi-demo-bucket'
)
print(response1)