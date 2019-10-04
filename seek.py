# developed by nchilaka
# this script writes to a file dst_file by seeking data from src_file at offset 0 and size of 1025 (ie to unalign with ec)
src_file = open("file", "r")
dst_file = open("dst_file", "a+")
for i in range(1000):
        src_file.seek(0, 0)
        dst_file.write(src_file.read(1025))
src_file.close()
dst_file.close()

"""
#e = random.randrange(1001, 100001, 2)
# developed by nchilaka
# this script writes to a file dst_file by seeking data from src_file at offset 0 and size of 1025 (ie to unalign with ec)
import random, time

for i in range(1, 1000000):
        dest_file = 'dest_file' + str(i)
        src_file = open("file", "r")
        dst_file = open(dest_file, "a+")
        for i in range(1000):
                e = random.randrange(1001, 100001, 2)
                src_file.seek(0, 0)
                dst_file.write(src_file.read(e))
        time.sleep(10)
        src_file.close()
        dst_file.close()

"""
