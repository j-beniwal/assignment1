#!/bin/bash

# Create a vpc with 10.0.0.0/16 CIDR BLOCK
aws ec2 create-vpc --cidr-block 10.0.0.0/16 --generate-cli-skeleton VPCid
# VPCid=$(jq '.Vpc | .[] | .VpcId' vpcout)


aws ec2 create-subnet --availability-zone us-east-1a --vpc-id VPCid --cidr-block 10.0.1.0/24
aws ec2 create-subnet --availability-zone us-east-1a --vpc-id VPCid --cidr-block 10.0.2.0/24
aws ec2 create-subnet --availability-zone us-east-1b --vpc-id VPCid --cidr-block 10.0.3.0/24
aws ec2 create-subnet --availability-zone us-east-1b --vpc-id VPCid --cidr-block 10.0.4.0/24
aws ec2 create-subnet --availability-zone us-east-1c --vpc-id VPCid --cidr-block 10.0.5.0/24
aws ec2 create-subnet --availability-zone us-east-1c --vpc-id VPCid --cidr-block 10.0.6.0/24

#igout=$(aws ec2 create-internet-gateway)
aws ec2 create-internet-geteway --generate-cli-skeleton igId
#igId=$(jq '.InternetGateway | .[] | .InternetGatewayId' igout)

# To attach the Internet Gateway to VPC
aws ec2 attach-internet-gateway --vpc-id VPCid --internet-gateway-id igId

# Create Coustem route table for VPC
aws ec2 create-route-table --vpc-id VPCid --generate-cli-skeleton RTb

# Create Route in the route table that points all traffic (0.0.0.0/0) to the internet gateway
aws ec2 create-route --route-table-id RTb --destination-cidr-block 0.0.0.0/0 --gateway-id igId

# To check if the routes are properly configured
aws ec2 describe-route-tables --route-table-id RTb

# Get the subnet ID to connet the route table to subnets
aws ec2 describe-subnets --filters "Name=vpc-id,Values=vpc-2f09a348" --query 'Subnets[*].{ID:SubnetId,CIDR:CidrBlock}' --generate-cli-skeleton SubID



