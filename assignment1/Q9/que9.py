##############################################################################
# Question 10:
# Write a program that creates your table “Games” in your AWS DynamoDB and adds certains items in the dynamo db. Example schema: 
# Schema “Games” :
# gid {Number}
# gname {String}
# publisher {String} 
# rating {Number}
# release_date {String}
# genres {String Set}
# Deliverable: Script
#############################################################################

import boto3
import time

import logging

#Initialize the logger
logging.basicConfig(filename="q9.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w') 
#Creating an object 
logger=logging.getLogger() 
#set logger to debug
logger.setLevel(logging.DEBUG) 

def create_games_table(dynamodb_client):
        dynamodb_client.create_table(
            AttributeDefinitions=[
                {
                    'AttributeName': 'gid',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'gname',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'rating',
                    'AttributeType': 'N'
                },
            ],
            TableName='GamesVS',
            KeySchema=[
                {
                    'AttributeName': 'gid',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'gname',
                    'KeyType': 'RANGE'
                },
            ],
            LocalSecondaryIndexes=[
                {
                    'IndexName': 'gdi_lsi',
                    'KeySchema': [
                        {
                            'AttributeName': 'gid',
                            'KeyType': 'HASH'
                        },
                        {
                            'AttributeName': 'rating',
                            'KeyType': 'RANGE'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'KEYS_ONLY'
                    },
                },
            ],
            BillingMode='PROVISIONED',
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        while True:
            dt_response = dynamodb_client.describe_table(TableName='GamesVS')
            if dt_response['Table']['TableStatus'] != 'ACTIVE':
                print("Waiting for table creation...")
                time.sleep(5)
            else:
                break


def add_items(dynamodb_client):
    response1 = dynamodb_client.put_item(
        TableName='GamesVS',
        Item={
            'gid': {
                'N': "1",
            },
            'gname': {
                'S': "Game-1",
            },
            'publisher': {
                'S': "wimbeldon",
            },
            'rating': {
                'N': "2",
            },
            'release_date': {
                'S': "31 Jun 2019",
            },
            'genres': {
                'SS': ['opencourt', 'smash'],
            }
        }
    )
    response2 = dynamodb_client.put_item(
        TableName='GamesVS',
        Item={
            'gid': {
                'N': "2",
            },
            'gname': {
                'S': "Game-1",
            },
            'publisher': {
                'S': "wimbeldon",
            },
            'rating': {
                'N': "1",
            },
            'release_date': {
                'S': "31 Jun 2019",
            },
            'genres': {
                'SS': ['opencourt', 'smash'],
            }
        }
    )
    response3 = dynamodb_client.put_item(
        TableName='GamesVS',
        Item={
            'gid': {
                'N': "3",
            },
            'gname': {
                'S': "Game-2",
            },
            'publisher': {
                'S': "wimbeldon",
            },
            'rating': {
                'N': "3",
            },
            'release_date': {
                'S': "2nd Jul 2019",
            },
            'genres': {
                'SS': ['defensive'],
            }
        }
    )
    response4 = dynamodb_client.put_item(
        TableName='GamesVS',
        Item={
            'gid': {
                'N': "2",
            },
            'gname': {
                'S': "Game-2",
            },
            'publisher': {
                'S': "wimbeldon",
            },
            'rating': {
                'N': "5",
            },
            'release_date': {
                'S': "2nd Jul 2019",
            },
            'genres': {
                'SS': ['smash', 'opencourt', 'defensive'],
            }
        }
    )
    print("Added items to table")


if __name__ == '__main__':
    dynamodb_client = boto3.client('dynamodb', region_name='us-east-1')
    create_games_table(dynamodb_client)
    add_items(dynamodb_client)
