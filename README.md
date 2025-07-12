# AWS Serverless Image Processor

A fully serverless image processing pipeline on AWS! Upload an image to S3, automatically process it with lambda and store the result in another S3 bucket and receives an email notification via SNS. I built this project to solve real-world problems like automating image preprocessing in document verification and content platforms and mostly to learn practical knowledge about AWS :) 

## Architecture 
<img src="assets/Architecture.webp" width="800"/>

## Key Features of the Project
1. S3
2. Lambda
3. SNS 

## How to run/use the application
- As of now I haven't yet deployed it. So, we need to run it manually in local. 
**Steps to run locally**
1. Clone the repo 
2. Open in VSCode and use the environment setup for easy installation.
3. after setting up the environemnt;
    - RUN: 
        1. `poetry run uvicorn main:app --reload` - Runs the FastAPI in the background
        2. Open a new terminal
        3. `poetry run python -m deploy.deploy_lambda` - creates the resources required
        4. Use `postman` or `curl` to upload objects to bucket and start the process. 