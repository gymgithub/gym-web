import boto3
import subprocess
import time
from sys import argv, stdout
import os

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
bucket_name = 'lofit-blog'
img_name = 'cloud.jpg'
def createBucket():
	#ec2_client.list_buckets()['Buckets']:
	try:
		s3_client.create_bucket(Bucket=bucket_name)
	except:
		print "This bucket already exists"

def uploadFiles(files):
	with open(files, 'w') as f:
		f.write('<html><head><title>Prueba</title></head><body><h1>Buenas tardes!!</h1>\
			<img src="https://s3.amazonaws.com/%s/%s"</body></html>' % (bucket_name, img_name))
	data = open(files, 'rb')
	data2 = open('/var/tmp/%s' % img_name, 'rb')
	data3 = open('/var/tmp/prueba.html')
	
	s3_resource.Bucket(bucket_name).put_object(Key=img_name, Body=data2, 
											   ContentType='image/jpeg', 
											   ACL='public-read')
	
	s3_resource.Bucket(bucket_name).put_object(Key='index.html', Body=data, 
											   ContentType='text/html', 
											   ACL='public-read')

	s3_resource.Bucket(bucket_name).put_object(Key='prueba.html', Body=data3, 
											   ContentType='text/html', 
											   ACL='public-read')

def downloadFiles(files):
	s3_resource.meta.client.download_file(bucket_name, 'index.html', files)

def deleteFiles():
	s3_client.delete_objects(Bucket=bucket_name, Delete={'Objects': [{'Key': 'prueba.html'}]})


def deleteBucket():
	s3_client.delete_bucket(Bucket=bucket_name)


if __name__ == '__main__':
	createBucket()
	uploadFiles('/var/tmp/index.html')
	#downloadFiles('/var/tmp/prueba.html')
	#deleteFiles()
	#deleteBucket()