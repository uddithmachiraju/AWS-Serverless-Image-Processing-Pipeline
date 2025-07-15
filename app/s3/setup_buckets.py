# File for creating the buckets and uploading files to buckets

import boto3 
import json 

def if_exists(client, bucket_name: str): 
    try: 
        client.head_bucket(Bucket = bucket_name)
        return True
    except:
        return False
    
def attach_bucket_policy(client, bucket_name, role_arn):
    bucket_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AllowLambdaGetAndPut",
                "Effect": "Allow",
                "Principal": {
                    "AWS": role_arn
                },
                "Action": ["s3:GetObject", "s3:PutObject"],
                "Resource": f"arn:aws:s3:::{bucket_name}/*"
            }
        ]
    }

    try: 
        client.put_bucket_policy(
            Bucket = bucket_name,
            Policy = json.dumps(bucket_policy) 
        )
        print(f"Attached policy to the Bucket: {bucket_name}")
    except Exception as e:
        print(f"Failed to attach bucket policy: {e}") 

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
