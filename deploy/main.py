import time 
from app.s3.setup_buckets import create_bucket_if_not_exists
from app.iam.role import create_iam_role 
from app.lambda_func.setup_lambda import create_lambda_function
from deploy.trigger import add_s3_trigger

bucket_1 = "bucket-1-5027" 
bucket_2 = "bucket-2-5027"
region = "ap-south-1" 

def deploy(filename = "tasks.txt", key = "tasks.txt"):
    bucket_1_response = create_bucket_if_not_exists(bucket_name = bucket_1, region = region) 
    bucket_2_response = create_bucket_if_not_exists(bucket_name = bucket_2, region = region)
    iam_role_response = create_iam_role(rolename = "lambda-s3-execution-role", region = region) 
    print("Waiting 60 seconds for IAM role to propagate...")
    time.sleep(60) 
    lambda_func_response = create_lambda_function(function_name = "AWSIPP", region = region, 
                           role_arn = iam_role_response["Role"]["Arn"], zip_path = "lambda_func.zip", handler = "handler.lambda_handler", 
                           runtime = "python3.12")
    print("Waiting 60 seconds for Lambda to propagate...")
    time.sleep(60) 
    trigger_response = add_s3_trigger("AWSIPP", lambda_func_response["FunctionArn"], bucket_1, region)  
 
if __name__ == "__main__":
    deploy()