import boto3
import subprocess
# first example

# creating the connection
#ec2 = boto3.resource('ec2')
ec2_client = boto3.client('ec2')


key_name = 'example_deploy'
security_name = 'example_security'
ami_id = 'ami-8311b8f0'
key_name2 = 'wordpress-blog-keypair'
# launch new instance
def CreateKeyPair():
	
	#command = 'aws ec2 create-key-pair --key-name %s --query "KeyMaterial" > "example_deploy.pem"' % key_name
	#process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
	#output, error = process.communicate()
	key_pair = ec2_client.create_key_pair(KeyName=key_name)

	with open('example_deploy.pem', 'w') as f:
		f.write(key_pair['KeyMaterial'])	

def CreateSecurityGroup():
	try:
		# Describe security groups to check if that group already exists
		ec2_client.describe_security_groups(GroupNames=[security_name])
	except:
		ec2_client.create_security_group(GroupName=security_name, Description='Trying python boto')
	
		ec2_client.authorize_security_group_ingress(GroupName='example_security', 
			IpPermissions=[{'IpProtocol': 'tcp', 'FromPort': 22, 'ToPort':22, 'IpRanges':[{'CidrIp': '0.0.0.0/0'}]},
					   {'IpProtocol': 'tcp', 'FromPort': 80, 'ToPort':80, 'IpRanges':[{'CidrIp': '0.0.0.0/0'}]}])


def LaunchInstance(zone):

	ec2_client.run_instances(ImageId=ami_id, MinCount=1, MaxCount=1, KeyName=key_name, 
							 SecurityGroups=[security_name], InstanceType='t1.micro', 
							 Placement={'AvailabilityZone': zone})

def ActionInstance():

	for i in ec2_client.describe_instances()['Reservations']:
		for m in i['Instances']:
			if m['KeyName'] == key_name or m['KeyName'] == key_name2:
				instance_id = m['InstanceId']
				print instance_id
				try:
					ec2_client.stop_instances(InstanceIds=[instance_id])
				except:
					print instance_id
					continue

if __name__ == '__main__':
	#c2_client.describe_key_pairs(KeyNames=[key_name])['KeyPairs']
	if ec2_client.describe_key_pairs(KeyNames=[key_name])['KeyPairs'] == []:
		CreateKeyPair()

	CreateSecurityGroup()
	#LaunchInstance('eu-west-1b')
	ActionInstance()
