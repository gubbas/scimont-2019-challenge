import boto3
import botocore

BUCKET_NAME = 'sm2019-social-media' # replace with your bucket name
KEY = 'raw/cnn_post_6.txt' # replace with your object key

s3 = boto3.resource('s3')

try:
    print('downloading ',KEY)
    s3.Bucket(BUCKET_NAME).download_file(KEY, 'cnn_post_6.txt')  # downloads to in same dir as script
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise