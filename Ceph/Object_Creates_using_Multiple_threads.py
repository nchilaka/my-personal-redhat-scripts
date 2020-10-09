'''
What this script Accomplishes:
Helps to create a "n x million"  objects in one bucket in a pool.
where n is "number of threads"
Prerequisites:
1) Setup the cluster
2) Have RGW nodes identified
3) Assign rgw node hostname to "host" variable in code(search for "$HOSTNAME")
4) Change the number of objects if you would like to; default is 1Million
5) Assign correct value of user, access and secret key instead of testuser2
'''

import threading
import time
import boto
import boto.s3.connection

user = "nchilaka"
access_key = "RIQJFU8K65ZA08TUNPG1"
secret_key = "fjcUH4MppQscKSnRdDxA44XKdQ8bzJUJCKmGimEj"
boto.config.add_section('s3')
conn = boto.connect_s3(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    host='f21-h17-000-r620.rgw',
    port=8080,
    is_secure=False,
    calling_format=boto.s3.connection.OrdinaryCallingFormat(),
)
bucket_name = 'megabucket'
bucket = conn.create_bucket(bucket_name)


def main_logic(tnum):
    '''
    user = "nchilaka"
    access_key = "RIQJFU8K65ZA08TUNPG1"
    secret_key = "fjcUH4MppQscKSnRdDxA44XKdQ8bzJUJCKmGimEj"
    boto.config.add_section('s3')
    conn = boto.connect_s3(
            aws_access_key_id = access_key,
            aws_secret_access_key = secret_key,
            host = 'f21-h17-000-r620.rgw',
            port = 8080,
            is_secure=False,
            calling_format = boto.s3.connection.OrdinaryCallingFormat(),
            )
    #print(str(user))
    # Creation of bucket using "user" as the name for bucket
    # In case you want to choose a name for the bucket change as below
    # bucket = conn.create_bucket('my-new-bucket')
    bname = 'megabucket'
    bucket = conn.create_bucket(bname)
    '''
    for i in range(1000000):
        file = 'dirx/dir' + tnum + '/' + str(user) + '_' + str(i) + '.txt'
        key = bucket.new_key(file)
        key.set_contents_from_string('tnum Screen job')
'''
    # This gets a list of objects in the bucket.
    for key in bucket.list():
        print("{name}\t{size}\t{modif}".format(name = key.name,
                                               size = key.size,
                                               modif = key.last_modified))


'''
if __name__ == "__main__":
    tlist = []
    for i in range(11):
        print(i)
        tnum = str(i)
        print(tnum)
        # titem = 'a' + tnum
        tlist.append(threading.Thread(target=main_logic, args=(tnum,)))
        print(tlist[i])
        tlist[i].start()
'''
try:
    threading.Thread(main_logic, ('1',))
    threading.Thread(main_logic, ('2',))
except:
   print "Error: unable to start thread"
'''
