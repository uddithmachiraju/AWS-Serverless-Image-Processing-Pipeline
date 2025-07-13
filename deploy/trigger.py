import boto3 

def add_s3_trigger(lambda_func_name, lambda_function_arn, bucket_name, region):
    s3_client = boto3.client("s3", region_name = region)
    lambda_client = boto3.client("lambda", region_name = region) 

    # Add permission to S3 to invoke lambda
    try:
        lambda_client.add_permission(
            FunctionName = lambda_func_name, 
            StatementId = f"{bucket_name}-s3-invoke",
            Action = "lambda:InvokeFunction",
            Principal = "s3.amazonaws.com",
            SourceArn = f"arn:aws:s3:::{bucket_name}" 
        )
    except Exception as e:
        print(f"Permission already exists: {e}") 

    # Setup the trigger when object is created 
    config = {
        "LambdaFunctionConfigurations": [
            {
                "LambdaFunctionArn": lambda_function_arn,
                "Events": ["s3:ObjectCreated:*"] 
            }
        ]
    }

    # Apply the configuration to the bucket
    response = s3_client.put_bucket_notification_configuration(
        Bucket = bucket_name,
        NotificationConfiguration = config 
    )

    print(f"Lambda trigger added for S3 bucket: {bucket_name}") 
    return response 