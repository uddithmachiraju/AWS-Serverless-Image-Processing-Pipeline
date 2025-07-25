#!/bin/bash 

# Set the name
BUCKET_1="bucket-1-5027"
BUCKET_2="bucket-2-5027"
LAMBDA="AWSIPP"
ROLE_NAME="lambda-s3-execution-role"
REGION="ap-south-1"
TOPIC_ARN="arn:aws:sns:us-east-1:847128339366:upload-notification"

echo "Started Cleaning..."

# 1. Delete the lambda function
echo "Deleting the Lambda function..." 
aws lambda delete-function --function-name $LAMBDA --region $REGION 

# 2. Empty and delete the S3 buckets
for BUCKET in $BUCKET_1 $BUCKET_2
do
    echo "Emptying bucket: $BUCKET" 
    aws s3 rm s3://$BUCKET --recursive --region $REGION 

    echo "Deleting the bucket: $BUCKET" 
    aws s3api delete-bucket --bucket $BUCKET --region $REGION 
done 

# 3. Detach and delete role
echo "Detaching the policies from IAM Role: $ROLE_NAME" 
aws iam detach-role-policy --role-name $ROLE_NAME --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
aws iam detach-role-policy --role-name $ROLE_NAME --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess
aws iam detach-role-policy --role-name $ROLE_NAME --policy-arn arn:aws:iam::aws:policy/AmazonSNSFullAccess

echo "Deleting the IAM Role: $ROLE_NAME" 
aws iam delete-role --role-name $ROLE_NAME --region $REGION 

# 4. Unsubscribe and delete SNS 
for sub in $(aws sns list-subscriptions-by-topic --topic-arn "$TOPIC_ARN" --query 'Subscriptions[].SubscriptionArn' --output text)
do
    echo "Unsubcribing the topic: $sub" 
    aws sns unsubscribe --subscription-arn "$sub"
done

aws sns delete-topic --topic-arn "$TOPIC_ARN"

echo "Cleanup completed.." 