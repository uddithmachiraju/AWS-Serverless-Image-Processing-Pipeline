# File for creating the buckets and uploading files to buckets

import boto3 

def if_exists(client, bucket_name: str): 
    try: 
        client.head_bucket(Bucket = bucket_name)
        return True
    except:
        return False

def create_bucket_if_not_exists(bucket_name: str, region: str): 
    s3_client = boto3.client("s3", region_name = region) 
    bucket_exists = if_exists(s3_client, bucket_name) 
    if not bucket_exists:
        try:
            if region == "us-east-1":
                response = s3_client.create_bucket(
                    Bucket = bucket_name
                )
            else:
                response = s3_client.create_bucket(
                    Bucket = bucket_name,
                    CreateBucketConfiguration = {
                        "LocationConstraint": region
                    }
                )
            print(f"Created a New Bucket {bucket_name}") 
            return response 
        except Exception as e:
            print(f"Failed to create bucket '{bucket_name}': {e}")
            return str(e)
    else: 
        print(f"Bucket already exists: {bucket_name}") 
