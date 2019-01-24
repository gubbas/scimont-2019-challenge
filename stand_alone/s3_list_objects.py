import boto3
import botocore

BUCKET_NAME = 'sm2019-social-media' # replace with your bucket name

s3 = boto3.resource('s3')

try:
    print('List Objects in  ',BUCKET_NAME)
    for obj in s3.Bucket(BUCKET_NAME).objects.all():
        print(obj.key)

except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise