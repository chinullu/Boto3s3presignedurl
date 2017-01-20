#!/usr/bin/python

#Import 
import boto3
#Validate Bucket name and keyphrases before running this program  
BUCKET = 'MyBucket'
KEY = 'KeyPhrases'
 
s3 = boto3.client('s3')
print s3.generate_presigned_url(
    ClientMethod='put_object',
    Params={'Bucket': BUCKET, 'Key': KEY},
    ExpiresIn=86400,#Here 86400 seconds means 60*60*24(1day) The url expires in 1 day
    HttpMethod='PUT')
  
