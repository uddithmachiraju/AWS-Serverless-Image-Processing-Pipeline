import boto3  

def create_lambda_function(function_name, region, role_arn, zip_path, handler, runtime, topic_arn):
    lambda_client = boto3.client("lambda", region_name = region) 

    # Need to pass the binary code to lambda 
    with open(zip_path, "rb") as file:
        zipped_code = file.read() 

    # Create a lambda function 
    try:
        response = lambda_client.create_function(
            FunctionName = function_name,
            Runtime = runtime, 
            Role = role_arn, 
            Handler = handler,
            Code = {
                "ZipFile": zipped_code
            },
            Timeout = 30,
            MemorySize = 128, 
            Environment={
                'Variables': {
                    'SNS_TOPIC_ARN': "arn:aws:sns:ap-south-1:847128339366:upload-notification"
                }
            }
        ) 
        print(f"Lambda Function Created: {function_name}")
        return response 
    except Exception as e:
        print(f"Exception: {e}") 
        return None 