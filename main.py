from fastapi import FastAPI
from api.models import S3Upload 
from app.s3.s3_utils import upload_files

app = FastAPI() 

@app.post("/upload") 
def upload_objects_to_s3(item: S3Upload):
    upload_files(item.bucket_name, item.filename, item.key) 
    return {
        "status": "success", 
    } 