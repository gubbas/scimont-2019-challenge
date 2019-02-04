from __future__ import print_function
import json
import urllib
import boto3

s3 = boto3.client('s3')
comprehend = boto3.client(service_name='comprehend')



def lambda_handler(event, context):
    print("Process TWEETS LAMDA STARTING : " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    #key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))
    key=event['Records'][0]['s3']['object']['key']
    # key='raw/cnn_post_8.txt'

    print('BUCKET NAME:',bucket)
    print('KEY:',key)
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE of the Object: " + response['ContentType'])

        text = s3.get_object(Bucket=bucket, Key=key)['Body'].read().decode('utf-8')
        print('RAW TEXT of FILE ',text)

        json_content = comprehend.detect_sentiment(Text=text, LanguageCode='en')
        print('Sentiment : ', json_content['Sentiment'])
        print('Sentiment Score Positve : ', json_content['SentimentScore']['Positive'])
        print('Sentiment Score Negative : ', json_content['SentimentScore']['Negative'])
        print('Sentiment Score Mixed : ', json_content['SentimentScore']['Mixed'])


        return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e