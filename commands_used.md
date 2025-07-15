## AWS CLI Commands
1. `aws s3 ls` - Lists the buckets. 
2. To delete a bucket. We need to do two things.
    1. Empty the bucket - `aws s3 rm <s3://bucket-name> --recursive`
    2. Delete the bucket - `aws s3api delete-bucket --bucket <bucket-name> --region <region>`
3. `aws s3 ls <bucket-name>` - Lists the objects in the bucket.
4. `aws s3api list-objects-v2 --bucket <bucket-name>` - get the information about the content in that bucket.
5. To delete an IAM role
    1. Lists down the attached policies - `aws iam list-attached-role-policies --role-name <role-name>` 
    2. Detach the policies first - `aws iam detach-role-policy --role-name <role-name> --policy-arn <policy-arn>`
    3. Delete the role - `aws iam delete-role --role-name <role-name>` 
6. `aws iam list-roles` - List down all the roles.
7. `aws lambda list-functions --region <region>` - Lists the functions in that region
8. `aws lambda delete-function --function-name <function-name> --region <region>` - Deletes a lambda function
9. `aws s3api get-bucket-policy --bucket <bucket-name>` - Get the Bucket policies 

## AWS Fuctions
1. `create_bucket` - Creates a bucket
2. `head_bucket` - Check if the bucket exists raises an Error if not else None
3. `upload_file` - Uploads the file to the bucket
4. `iam_client.create_role` - Creates an IAM Role
5. `iam_client.attach_role_policy` - Attached policies to the role. 
6. `lambda_client.create_function` - Creates a lambda function. 
7. `lambda_client.add_permission` - Grants permission to another AWS service. 
8. `s3_client.put_bucket_notification_configuration` - Configure S3 bucket to trigger events and notify a destination.
9. `iam_clinet.get_role` - Retrieves details of an existing IAM role
10. `s3_client.get_object` - 
11. `s3_client.put_object` - 
12. `s3_client.put_bucket_policy` - Adds a policy to the bucket. 