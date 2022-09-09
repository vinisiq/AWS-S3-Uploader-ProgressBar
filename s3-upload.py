import boto3
import tqdm
import os

# S3 Uploader with Progress Bar

s3_response = boto3.resource('s3')


def upload_s3(bucket, key, filename):
    #Bucket: the name of your bucket on AWS S3
    #Key: the name that you want to use in your bucket
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
