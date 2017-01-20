#!/usr/bin/python
 
import boto3
 
BUCKET = 'YOUR_BUCKET_NAME'
KEY = 'YOUR_KEY'
 
s3 = boto3.client('s3')
print s3.generate_presigned_url(
    ClientMethod='put_object',
    Params={'Bucket': BUCKET, 'Key': KEY},
    ExpiresIn=86400,
    HttpMethod='PUT')
  
