#################################################################################
# Question 10
# Write a program that reads your table “Games” from your AWS DynamoDB and
# Returns only the game where ‘gid=2’ (“Query” Feature DynamoDB).
# Prints out the ‘gname’ and the ‘rating’ only.
################################################################################

import boto3
from boto3.dynamodb.conditions import Key, Attr

import logging

#Initialize the logger
logging.basicConfig(filename="Q10.log", format='%(asctime)s %(message)s', filemode='a')

logger=logging.getLogger()
#set logger to debug
logger.setLevel(logging.DEBUG)

# Get the service resource.
dynamodb = boto3.resource('dynamodb' , region_name='us-east-1')
logger.info("Table geting Created ..........")
table = dynamodb.Table('JeevansGame')

#Conditional query
logger.info("Finding Object .......")
response = table.query(
    KeyConditionExpression=Key('gid').eq(2))

logger.info("Ola! Data is here")
for i in response['Items']:
	print(i['gname'] , i['rating'])
