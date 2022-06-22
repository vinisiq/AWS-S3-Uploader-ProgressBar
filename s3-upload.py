import boto3
import tqdm
import os

# S3 Uploader with Progress Bar

'''
To use this code you need to use AWS CLI. Type 'aws configure' on your terminal and paste your user
acess key and your password key. If you don't have a user key you can made this on IAM > Users > 
Create New User. Use the policies Billing and AdministratorAccess.

The best way to make your datalake in AWS Cloud is using the us-east-1 in your buckets, because 
if you try to integrate your buckets with other products in AWS (like EMR) maybe it can not
work well.

'''
s3_response = boto3.resource('s3')


def upload_s3(bucket, key, filename):
    #Bucket: the name of your bucket on AWS S3
    #Key: the name that you want to use on your bucket
    #Filename: the name of the file here, in your machine

    file_size = os.stat(filename).st_size
    s3 = boto3.client('s3')
    print('')
    print('Available Buckets:')
    
    for bckt in s3_response.buckets.all():
        print(f'- {bckt.name}')
    print('')

    print(f'Upload of {filename} starting... ')
    print('')
    with tqdm.tqdm(total=file_size, unit="B", unit_scale=True, desc=filename) as pbar:
        s3.upload_file(
            Filename=filename,
            Bucket=bucket,
            Key=key,
            Callback=lambda bytes_transferred: pbar.update(bytes_transferred),
        )
    print('')
    print(f'Upload of {filename} performed on the Bucket: {bucket}')
    print('')


bucket = str(input('Type your bucket: '))
key = str(input('Type the name of your file in AWS S3: '))
filename = str(input('Type the path of your file: '))

upload_s3(bucket, key, filename)

'''

    You can comment or exclud the inputs if you want to use the function method, for example:   
    upload_s3("datalake-enem2020-vinisiq", "teste", "data/kkkkk.txt") 

'''