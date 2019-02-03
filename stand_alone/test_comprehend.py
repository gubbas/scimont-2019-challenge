# Examples : https://docs.aws.amazon.com/comprehend/latest/dg/get-started-api-sentiment.html#get-started-api-sentiment-python


import boto3
import json

#comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')

comprehend = boto3.client(service_name='comprehend')

BUCKET_NAME = 'sm2019-social-media' # replace with your bucket name
KEY = 'raw/cnn_post_7.txt' # replace with your object key

s3_client = boto3.client(service_name='s3', region_name='us-east-1')

#text = "It is raining today in Seattle"

text = s3_client.get_object(Bucket=BUCKET_NAME, Key=KEY)['Body'].read().decode('utf-8')

print(text)

print('Calling DetectSentiment')
json_content = comprehend.detect_sentiment(Text=text, LanguageCode='en')

#print(json_content)

print('Sentiment : ',json_content['Sentiment'])
print('Sentiment Score Positve : ',json_content['SentimentScore']['Positive'])
print('Sentiment Score Negative : ',json_content['SentimentScore']['Negative'])
print('Sentiment Score Mixed : ',json_content['SentimentScore']['Mixed'])

#print(json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
print('End of DetectSentiment\n')