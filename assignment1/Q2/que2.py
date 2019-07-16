##############################################################################
# Question 2:
# Assuming you have a versioning enabled S3 bucket and multiple versions of the same object, 
# Write a python script which takes the bucket name and object path as parameters 
# and downloads the 2nd latest version of this object i.e the one prior to the latest version.
##############################################################################


import boto3
import logging

#Initialize the logger
logging.basicConfig(filename="q2.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w') 
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG) 

#setting up s3 as resource
s3=boto3.resource('s3')

#take input from the user
bucket_name=input("Bucket name:")
object_name=input("Object name:")

# get all the versons of the object in list named versions
versions = s3.Bucket(bucket_name).object_versions.filter(Prefix=object_name)

# collect the versionId from the versions
version_id=[version.get()['VersionId'] for version in versions]
s3_client = boto3.client('s3')

# download the second latest verson using its verson id from the list of versons
s3_client.download_file(bucket_name, object_name, '/home/ubuntu/newfile.txt', ExtraArgs={'VersionId':version_id[1] })

print("second latest verson downloaded")
