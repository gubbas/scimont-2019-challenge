# Example : https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3.html

import os
import sys
import threading

import boto3

class ProgressPercentage(object):
    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()
    def __call__(self, bytes_amount):
        # To simplify we'll assume this is hooked up
        # to a single filename.
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()


# Get the service client
s3 = boto3.client('s3')

BUCKET_NAME = 'sm2019-social-media' # replace with your bucket name
KEY = 'raw/cnn_post_7.txt' # replace with your object key
FILE_NAME='test_tweet_content.txt'
#FILE_NAME='../test_data/test_tweet_content.txt'

# Upload tmp.txt to bucket-name at key-name
s3.upload_file(
    FILE_NAME, BUCKET_NAME, KEY,
    Callback=ProgressPercentage(FILE_NAME))