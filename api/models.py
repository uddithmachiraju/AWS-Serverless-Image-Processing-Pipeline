from pydantic import BaseModel

class S3Upload(BaseModel):
    bucket_name: str 
    filename: str 
    key: str 