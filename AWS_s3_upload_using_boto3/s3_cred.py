import boto3
import os

# ---- creating s3 bucket -----
def create_s3bucket(bucket_name, region):

    try:
        s3 = boto3.client('s3', region_name = region)
        s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration = {'LocationConstraint':region})
        print(f"s3bucket {bucket_name} created successfully in region {region}")
        return bucket_name
    except Exception as e:
        print(f"error occured while creating s3 bucket {e}")
        return None
    

bucket_name = 'boto3-source-bucket'
region = 'ap-south-1'
create_s3bucket(bucket_name,region)