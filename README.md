# Boto3s3presignedurl
using boto3 create an S3 presigned URL with an expiration date of 1 day


Execute the above python script as follows ./s3.py  or as follows python s3.py

This will print the presigned url on shell screen

Sample URL:

https://YOUR_BUCKET.s3.amazonaws.com/YOUR_KEY?AWSAccessKeyId=AKIAIXXXXXXXXXXXXXXX&Expires=86400&Signature=wfs8QjbToDFannh6po33DAxvO34%3D


To test the script you have to follow below steps:

a) Create a new sample file test.txt

$ echo abcde > test.txt

b) Use curl command to upload test.txt file to S3 using PUT method and Presigned URL generated earlier

$ curl -D - -X PUT --upload-file test.txt 'https://YOUR_BUCKET.s3.amazonaws.com/YOUR_KEY?AWSAccessKeyId=AKIAIXXXXXXXXXXXXXXX&Expires=86400&Signature=wfs8QjbToDFannh6po33DAxvO34%3D'

c) After executing the above curl command you should see an output containing

HTTP/1.1 100 Continue
HTTP/1.1 200 OK

This means the file has successfully uploaded to S3 bucket, Now login into AWS console and navigate to S3 bucket to check the file.

Thank you.
