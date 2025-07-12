import boto3 

s3_client = boto3.client("s3") 

def upload_files(bucket_name: str, filename: str, key: str):
    try:
        s3_client.upload_file(
            filename, bucket_name, key 
        ) 
        print(f"Uploaded files to {bucket_name} from {filename} named as {key}") 
    except Exception as e:
        print(f"Failed to upload file: {e}") 