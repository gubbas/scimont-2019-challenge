# Example : https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3.html

import boto3
import botocore

BUCKET_NAME = 'sm2019-social-media' # replace with your bucket name
KEY = 'raw/cnn_post_6.txt' # replace with your object key

s3 = boto3.resource('s3')

try:
    print('Reading file  ',KEY)
    response = s3.get_object(Bucket=BUCKET_NAME, Key=KEY)
    emailcontent = response['Body'].read().decode('utf-8')

    print (emailcontent)


except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise