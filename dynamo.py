import boto3

s3 = boto3.resource("s3")
s3_bucket_name = ""
for bucket in s3.buckets.all():
    s3_bucket_name = bucket.name
    print(bucket.name)

with open("737474.png", "rb") as data:
    s3.Bucket(s3_bucket_name).put_object(Key="test.jpg", Body=data)

