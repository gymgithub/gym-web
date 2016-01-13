import boto3
import subprocess
import time
from sys import argv, stdout
import os

elb_client = boto3.client('elb')
elb_name = 'wordpress-blog-elb'
ec2_client = boto3.client('ec2')
key_name2 = 'wordpress-blog-keypair'
key_name = 'example_deploy'

def createElb():
	elb_client.create_load_balancer(LoadBalancerName=elb_name,
									Listeners=[{'Protocol': 'http', 'LoadBalancerPort': 80,
									'InstanceProtocol': 'http', 'InstancePort': 80}],
									AvailabilityZones=['eu-west-1a', 'eu-west-1b'])

def registerInstances():
	for i in ec2_client.describe_instances()['Reservations']:
		for m in i['Instances']:
			if m['KeyName'] == key_name or m['KeyName'] == key_name2:
				instance_id = m['InstanceId']
				try:
					elb_client.register_instances_with_load_balancer(LoadBalancerName=elb_name,
						Instances=[{'InstanceId': instance_id}])
				except:
					continue

def elbStatus(full=False):
	if full == False:
		elb_info = elb_client.describe_load_balancers()['LoadBalancerDescriptions'][0]['DNSName']

	else:
		elb_info = elb_client.describe_load_balancers()

	return elb_info

if __name__ == '__main__':
	createElb()
	registerInstances()
	print elbStatus()