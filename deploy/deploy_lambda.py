from app.s3.setup_buckets import create_bucket_if_not_exists
from app.iam.role import create_iam_role

bucket_1 = "bucket-1-5027" 
bucket_2 = "bucket-2-5027"

def deploy(filename = "tasks.txt", key = "tasks.txt"):
    create_bucket_if_not_exists(bucket_name = bucket_1, region = "ap-south-1") 
    create_bucket_if_not_exists(bucket_name = bucket_2, region = "ap-south-1") 
    create_iam_role(rolename = "lambda-s3-execution-role") 

if __name__ == "__main__":
    deploy()