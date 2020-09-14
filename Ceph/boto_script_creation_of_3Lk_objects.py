import boto
import boto.s3.connection
import re

'''
"user": "testuser2",
"access_key": "XT2P5T16LNYOGQU9SOID",
"secret_key": "W1GtGK7AE5A4eNHcfqHiV7DThCiOwDQmArOJCUQM"
'''
users = []
access_keys = []
secret_keys = []
i = 4
# uidlist.log
f = open("uidlist.log", "r")
# print(f.readline())
# '''
for line in f:
    # print(line)
    if i % 3 == 1:
        users.append(line.rstrip("\n").split(": ")[-1].strip(',').strip('"'))
    elif i % 3 == 2:
        access_keys.append(line.rstrip("\n").split(": ")[-1].strip(',')
                           .strip('"'))
    elif i % 3 == 0:
        secret_keys.append(line.rstrip("\n").split(": ")[-1].strip(',')
                           .strip('"'))
    else:
        pass
    i = i + 1
print(users)
print(access_keys)
print(secret_keys)
# '''


# [root@f13-h20-b07-5039ms ~]# cat bigbuck.py
# import boto
# import boto.s3.connection

# access_key = $access
# secret_key = $secret
# access_key = "U7VW5EAC9TYWK51R834C"
# secret_key = "3TvjetkBQNXOBtUpvCeWcfj0lA3W75vOeX8dUQWj"

boto.config.add_section('s3')
for user,access_key,secret_key in zip(users,access_keys,secret_keys):
    conn = boto.connect_s3(
            aws_access_key_id = access_key,
            aws_secret_access_key = secret_key,
            host = 'f13-h20-b07-5039ms.rdu2.scalelab.redhat.com',
            port = 8080,
            is_secure=False,
            calling_format = boto.s3.connection.OrdinaryCallingFormat(),
            )
    #print(str(user))
    bucket = conn.create_bucket(str(user))
    for bucket in conn.get_all_buckets():
        print("{name}\t{created}".format(name = bucket.name,
                                         created = bucket.creation_date))
    for i in range(500, 300000):
        file = str(user) + '_' + str(i) + '.txt'
        key = bucket.new_key(file)
        key.set_contents_from_string('Hello World!')

    for key in bucket.list():
            print("{name}\t{size}\t{modif}".format(name = key.name,
                                                   size = key.size,
                                                   modif = key.last_modified))
