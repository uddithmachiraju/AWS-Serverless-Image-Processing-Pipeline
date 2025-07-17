import boto3 
import json
from PIL import Image 
import io 
import os 
from app.sns.setup_sns import send_sns_notification

s3_client = boto3.client("s3") 

def lambda_handler(event, context): 
    print(f"lambda function triggered: {json.dumps(event)}")
    
    # Get the bucket and object key from event
    source_bucket = event["Records"][0]["s3"]["bucket"]["name"] 
    object_key = event["Records"][0]["s3"]["object"]["key"] 
    target_bucket = "bucket-2-5027"

    # Get the file from s3 
    object_ = s3_client.get_object(Bucket = source_bucket, Key = object_key) 
    print(object_) 
    data = object_["Body"].read()

    # Process the image
    image = Image.open(io.BytesIO(data)).convert("L")
    output_buffer = io.BytesIO()
    image.save(output_buffer, format = "PNG")
    output_buffer.seek(0) 

    # Upload the processed image ot bucket-2
    s3_client.put_object(
        Bucket = target_bucket, 
        Key = object_key,
        Body = output_buffer,
        ContentType = "image/png"
    ) 

    send_sns_notification(bucket_name = target_bucket, image_key = object_key)

    return {
        "Status" : 200,
        "Body" : f"Processed Image saved at {source_bucket}/{object_key}"
    }