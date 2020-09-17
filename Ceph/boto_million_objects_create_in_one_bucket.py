'''
What this script Accomplishes:
Helps to create a million  objects in one bucket in a pool.

Prerequisites:
1) Setup the cluster
2) Have RGW nodes identified
3) Assign rgw node hostname to "host" variable in code(search for "$HOSTNAME")
4) Change the number of objects if you would like to; default is 1Million
5) Assign correct value of user, access and secret key instead of testuser2
'''
# import boto
import boto.s3.connection

user = "testuser2",
access_key = "XT2P5T16LNYOGQU9SOID",
secret_key = "W1GtGK7AE5A4eNHcfqHiV7DThCiOwDQmArOJCUQM"

boto.config.add_section('s3')
conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
        host = '$HOSTNAME',
        port = 8080,
        is_secure=False,
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )
#print(str(user))
# Creation of bucket using "user" as the name for bucket
# In case you want to choose a name for the bucket change as below
# bucket = conn.create_bucket('my-new-bucket')

bucket = conn.create_bucket(str(user))
for i in range(1000000):
    file = str(user) + '_' + str(i) + '.txt'
    key = bucket.new_key(file)
    key.set_contents_from_string('Hello World!')

# This gets a list of objects in the bucket.
    for key in bucket.list():
            print("{name}\t{size}\t{modif}".format(name = key.name,
                                                   size = key.size,
                                                   modif = key.last_modified))