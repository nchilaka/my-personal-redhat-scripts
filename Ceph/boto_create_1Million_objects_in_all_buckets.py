'''
What this script Accomplishes:
Helps to create Lakhs of objects in list of buckets available in a pool.
'''

'''
Prerequisites:
1) Setup the cluster
2) Have RGW nodes identified
3) Assign rgw node hostname to "host" variable in code(search for "$HOSTNAME")
4) Change the number of objects if you would like to; default is 1million
5) The buckets should have a pattern and sequence eg: b1, b2, b3, etc
6) Users should have been created and the credentials saved to a file. If not 
the below shell script can help achieve the same
for i in {1..500};do radosgw-admin user create --uid="testuser$i" \
--display-name="testuser$i" |& tee -a uidcreate.log;
echo "###"|& tee -a uidcreate.log;done;
cat uidcreate.log |egrep "user|access_key|secret_key" >>uidlist.log
'''

import boto
import boto.s3.connection

# Creating lists to capture users, access_keys and secret_keys
users = []
access_keys = []
secret_keys = []
i = 4 # setting this to 4 for parsing and getting elements for above 3 lists
# Read the list of users, access keys, secret keys.
# Below is a snippet of contents of the file "uidlist.log"
'''
"user": "testuser499",
"access_key": "97A5IB7D8BX3KG9FUJAW",
"secret_key": "GDHaBukKABZuD3t6T8dM9mQLNnwnAK03iUQk7DTV"
"user": "testuser500",
"access_key": "3TXIB5ZS5FDTDPM1UJAJ",
"secret_key": "fJPjdnGAOwCLJPDRuvDPv1IlUlTpfJzuhchMCsGv"
'''
f = open("uidlist.log", "r")
# print(f.readline())

# Below code gets list of all the elements and appends to resp. lists
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

'''
Mention the RGW hostname to create the object in below host location
'''
boto.config.add_section('s3')
for user,access_key,secret_key in zip(users,access_keys,secret_keys):
    conn = boto.connect_s3(
            aws_access_key_id = access_key,
            aws_secret_access_key = secret_key,
            host = '$HOSTNAME',
            port = 8080,
            is_secure=False,
            calling_format = boto.s3.connection.OrdinaryCallingFormat(),
            )
    #print(str(user))
    bucket = conn.create_bucket(str(user)) # create bucket using username
    # Getting list of buckets and printing them
    for bucket in conn.get_all_buckets():
        print("{name}\t{created}".format(name = bucket.name,
                                         created = bucket.creation_date))
    # Creating 3Lk objects with object name eg: "user_1.txt"
    # Contents of the object is "Hello World!"
    for i in range(1000000):
        file = str(user) + '_' + str(i) + '.txt'
        key = bucket.new_key(file)
        key.set_contents_from_string('Hello World!')
    # This gets a list of objects in the bucket.
    for key in bucket.list():
            print("{name}\t{size}\t{modif}".format(name = key.name,
                                                   size = key.size,
                                                   modif = key.last_modified))

'''
 To list number of objects under a bucket, it would by default print only 
 1k objects. If you want total count, then specify as below using max-entries 
 "radosgw-admin bucket list --bucket=my-new-bucket --max-entries=100000000 \
 |grep accounted_size|wc -l"
'''