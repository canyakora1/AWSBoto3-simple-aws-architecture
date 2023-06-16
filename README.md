# AWSBoto3-simple-aws-architecture

## Brief Project Outline ##

Deploying a simple AWS architecture usine Boto3 which would include:

    A VPC
    Two Subnets (One Private and One Public)
    Routle table for each subnets
    Security Groups for all instances (EC2) deployed in each subnet
    One Internet gateway
    One ec2 instance in the public subnet and two instances in the private subnet

## Layout of the design ##

In the code above, we first create an EC2 resource using boto3.resource('ec2'). 
This resource provides a higher-level interface to interact with EC2.

We then create a VPC using create_vpc and a subnet within the VPC using create_subnet. 
We also create a security group using create_security_group and authorize inbound traffic 
on ports 22 (SSH) and 80 (HTTP).

Next, we launch an EC2 instance within the subnet using create_instances. Replace 'ami-12345678' 
with the desired AMI ID. The instance is associated with the previously created security group.

Finally, we create an S3 client using boto3.client('s3') and create an S3 bucket using create_bucket.

Remember to customize the code with your desired values, such as AMI ID, VPC CIDR block, subnet CIDR block, 
security group rules, and bucket name.

This is a basic example to give you an idea of how to build a detailed AWS architecture using Boto3. 
Depending on your requirements, you may need to modify and expand the code accordingly.