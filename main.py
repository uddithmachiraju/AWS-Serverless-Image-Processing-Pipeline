from fastapi import FastAPI
from api.models import S3Upload 
from deploy.deploy_lambda import deploy

app = FastAPI() 

@app.post("/upload") 
def upload_objects_to_s3(item: S3Upload):
    deploy(item.bucket_name, item.region, item.filename, item.key) 
    return {
        "status": "success", 
    }