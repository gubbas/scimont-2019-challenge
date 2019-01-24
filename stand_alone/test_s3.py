# Examples
# https://github.com/boto/boto3/blob/develop/boto3/examples/s3.rst

import boto3

s3 = boto3.resource('s3')

# List buckets in your account
for bucket in s3.buckets.all():
        print(bucket.name)



# List top-level common prefixes in Amazon S3 bucket
client = boto3.client('s3')
paginator = client.get_paginator('list_objects')
result = paginator.paginate(Bucket='gubba-s3-lamda-test', Delimiter='/')
for prefix in result.search('CommonPrefixes'):
    print(prefix.get('Prefix'))


# Restore Glacier objects in an Amazon S3 bucket