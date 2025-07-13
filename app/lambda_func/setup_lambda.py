import boto3  

def create_lambda_function(function_name, region, role_arn, zip_path, handler, runtime):
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
        ) 
        print(f"Lambda Function Created: {function_name}")
        return response 
    except Exception as e:
        print(f"Exception: {e}") 
        return None 