import boto3 
import json

def create_iam_role(rolename, region):
    iam_client = boto3.client("iam", region_name = region)

    # Define policy to the Role
    assume_role_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "lambda.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }

    # Create an IAM Role
    try:
        response = iam_client.create_role(
            RoleName = rolename,
            AssumeRolePolicyDocument = json.dumps(assume_role_policy),
            Description = "IAM Role for Lambda Execution"
        )

        # Add policies 
        # 1. CloudWatch 
        iam_client.attach_role_policy(
            RoleName = rolename,
            PolicyArn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
        )

        # 2. S3 Read only access 
        iam_client.attach_role_policy(
            RoleName = rolename,
            PolicyArn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
        )
        print(f"IAM Role Created with name: {rolename}") 
        return response
    except iam_client.exceptions.EntityAlreadyExistsException:
        print(f"IAM Role '{rolename}' already exists, returning existing role info.")
        return iam_client.get_role(RoleName=rolename) 