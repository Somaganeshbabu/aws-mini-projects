import json
import os
import boto3

s3_client = boto3.client('s3')

source_bucket_name = 'my-uploadedimages'
destination_bucket_name = 'destination-bucket-lambda'

def lambda_handler(event, context):
    response = s3_client.list_objects_v2(Bucket = source_bucket_name)
   
    for obj in response.get('Contents', []):
        source_key = obj['Key']
        
        if not object_exists_in_destination(source_key):
            copy_source = {'Bucket':source_bucket_name, 'Key':source_key}
            destination_key = os.path.basename(source_key)
            destination_object = {'Bucket':destination_bucket_name, 'Key':destination_key}
            try:
                s3_client.copy_object(CopySource =copy_source, Bucket = destination_object['Bucket'], Key=destination_object['Key'])
                print(f"Successfully copied {source_key} from {source_bucket_name} to {destination_bucket_name}")
            except Exception as e:
                print(f"Error copying {source_key} from {source_bucket_name} to {destination_bucket_name}: {e}")
        else:
            print(f"Object {source_key} already exists in {destination_bucket_name}")
    return{
        'statusCode': 200,
        'body': 'Images copied to destination bucket successfully.'
    }

def object_exists_in_destination(object_key):
    try:
        s3_client.head_object(Bucket=destination_bucket_name, Key=object_key)
        return True
    except Exception as e:
        return False