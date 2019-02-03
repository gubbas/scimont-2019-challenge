# Example : https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3.html
# https://stackoverflow.com/questions/42809096/difference-in-boto3-between-resource-client-and-session?noredirect=1&lq=1

import boto3
import botocore
import json

BUCKET_NAME = 'sm2019-social-media' # replace with your bucket name
KEY = 'raw/cnn_post_6.txt' # replace with your object key

#############################
# USER DEFINED FUNCTIONS HERE
############################

# just pass the instantiated bucket object
def list_bucket_contents(bucket):
    try:
        for object in bucket.objects.all():
            print(object.key)
            print(object)
            body = object.get()['Body'].read()
            print(body)

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise



# just pass the instantiated bucket object
def read_s3_object_contents(s3_obj):

    try:
        print('PRINING OBJECT CONTENTS')
        #print('Reading file  ',s3_obj.key)
        body = s3_obj['Body']
        file_content = body.read().decode('utf-8')
        print(file_content)

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

######################
# MAIN LOGIC STARTS HERE
######################

try:
    print('Reading file  ',KEY)

    # Obtain AWS Session
    my_east_sesison = boto3.Session(region_name='us-east-1')

    # Obtain Particular AWS Client
    #my_east_client = boto3.client('s3')
    my_east_client = my_east_sesison.client('s3')

    # my_east_client = boto3.client(service_name='s3', region_name='us-east-1')
    #my_east_client = boto3.client("s3", region_name='us-east-1')  # Directly get Client


    #Obtain Object
    s3_object = my_east_client.get_object(Bucket=BUCKET_NAME, Key=KEY)
    read_s3_object_contents(s3_object)

    ######################
    # SECOND METHOD
    ######################


    s3 = boto3.resource('s3')  # High level S3 session
    # alternate way to initialize session
    #my_east_sesison = boto3.Session(region_name='us-east-1')
    #s3 = my_east_sesison.resource('s3')

    # READ Contents of a bucket
    the_bucket = s3.Bucket(BUCKET_NAME)
    list_bucket_contents(the_bucket)




   # print(s3_obj)
    #body = s3_obj['Body']
    #print(body.read())

   # obj = my_s3c.get_object(Bucket=BUCKET_NAME, Key=KEY)
   #j = json.loads(obj['Body'].read())   #Python 2.7
   #j = json.loads(obj['Body'].read().decode('utf-8'))
   # j = json.loads(obj.get()['Body'].getvalue().decode('utf-8'))
   # print(j);
   # response = s3.get_object(Bucket=BUCKET_NAME, Key=KEY)
   # emailcontent = response['Body'].read().decode('utf-8')
   # print (emailcontent)


except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise