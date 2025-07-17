import boto3
import os 

def create_sns_topic(topic_name):
    sns_client = boto3.client("sns", region_name = "ap-south-1")
    response = sns_client.create_topic(
        Name = topic_name
    )
    topic_arn = response["TopicArn"]
    print(f"Created topic: {topic_name}") 
    return topic_arn

def subscribe_email_to_topic(topic_arn, email_address):
    sns_client = boto3.client("sns", region_name = "ap-south-1")
    sns_client.subscribe(
        TopicArn = topic_arn,
        Protocol = "email",
        Endpoint = email_address
    )
    print(f"Email subscription request sent to {email_address}. Conform it.") 

def send_sns_notification(bucket_name, image_key):
    sns_client = boto3.client("sns", region_name = "ap-south-1")
    topic_arn = os.environ["SNS_TOPIC_ARN"] 

    message = f"Image {image_key} has been processed and stored in bucket {bucket_name}" 
    subject = "Image Process Complete AWSIPP"

    sns_client.publish(
        TopicArn = topic_arn,
        Message = message,
        Subject = subject 
    )