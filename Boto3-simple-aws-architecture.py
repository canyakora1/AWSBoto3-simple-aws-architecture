import boto3

# CReate an EC2 resource
ec2_resource = boto3.resource('ec2')

# Create a VPC
vpc = ec2_resource.create_vpc(CidrBlock='10.0.0.0/16')
vpc.create_tags(Tags=[{'Key': 'Name', 'Value': 'DCGPlayroom'}])
vpc.wait_until_available()
print("VPC created:", vpc.id)

#Create a subnet within the VPC
public_subnet = ec2_resource.create_subnet(CidrBlock='10.0.1.0/24', VpcId=vpc.id)
public_subnet.create_tags(Tags=[{'Key': 'Name', 'Value': 'Public_subnet'}])
print("Subnet created:", public_subnet.id)

private_subnet = ec2_resource.create_subnet(CidrBlock='10.0.2.0/24', VpcId=vpc.id)
private_subnet.create_tags(Tags=[{'Key': 'Name', 'Value': 'Private_subnet'}])
print("Subnet created:", private_subnet.id)

#Create an Internet Gateway
internet_gateway = ec2_resource.create_internet_gateway(
    
)

# Create a security group
public_security_group = ec2_resource.create_security_group(
    GroupName='MySecurityGroup',
    Description='Allow ssh and http',
    VpcId=vpc.id
)
public_security_group.authorize_ingress(
    IpPermissions=[
        {'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'tcp', 'TpRanges': [{'CidrIp': '0.0.0.0/0'}]},
        {'FromPort': 80, 'ToPort': 80, 'IpProtocol': 'tcp', 'TpRanges': [{'CidrIp': '0.0.0.0/0'}]}
    ]
)
print("Security group created:", public_security_group.id)

private_security_group = ec2_resource.create_security_group(
    GroupName='MySecurityGroup',
    Description='Allow ssh and http',
    VpcId=vpc.id
)
private_security_group.authorize_ingress(
    IpPermissions=[
        {'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'tcp', 'TpRanges': [{'CidrIp': '0.0.0.0/0'}]},
        {'FromPort': 80, 'ToPort': 80, 'IpProtocol': 'tcp', 'TpRanges': [{'CidrIp': '0.0.0.0/0'}]}
    ]
)
print("Security group created:", private_security_group.id)

# Launch two ec2Instance, each in both subnets
public_ec2_instance = ec2_resource.create_instance(
    ImageId=
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    SubnetId=public_subnet.id,
    SecurityGroupIds=[public_security_group.id]
)[0]
public_ec2_instance.wait_until_running()
print("EC2 instance created:", public_ec2_instance.id)

private_ec2_instance = ec2_resource.create_instance(
    ImageId=
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    SubnetId=private_subnet.id,
    SecurityGroupIds=[private_security_group.id]
)[0]
private_ec2_instance.wait_until_running()
print("EC2 instance created:", private_ec2_instance.id)

# Create an s3 client
s3 = boto3.client('s3')

# Create an s3 bucket
bucket_name = 'dcgmedia-bucket-public'
print("Bucket created:", bucket_name)




