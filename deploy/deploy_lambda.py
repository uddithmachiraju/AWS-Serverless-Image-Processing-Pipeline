from app.s3.setup_buckets import upload_files

def deploy(bucket_name, region, filename, key):
    upload_files(bucket_name = "image-processing-bucket-1-5027", region = "ap-south-1", 
                 filename = "tasks.txt", key = "tasks.txt")

if __name__ == "__main__":
    deploy()