# Examples
# https://github.com/boto/boto3/blob/develop/boto3/examples/s3.rst

import boto3

s3 = boto3.resource('s3')

# List buckets in your account
for bucket in s3.buckets.all():
        print(bucket.name)

