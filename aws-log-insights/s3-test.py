from aws_auth import get_aws_session

session = get_aws_session()

# Now you can use this session to interact with AWS services
s3 = session.client('s3')

# Example: List all S3 buckets
response = s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]
print("Bucket List:", buckets)