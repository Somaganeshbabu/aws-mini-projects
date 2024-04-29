import boto3

s3 = boto3.client('s3', region_name= 'ap-south-1')
bucket_name= 'my-uploadedimages'
file_path = '/workspaces/aws-mini-projects/AWS_s3_upload_using_boto3/images/image1.jpg'

s3.upload_file(file_path, bucket_name, 'image1.jpg')