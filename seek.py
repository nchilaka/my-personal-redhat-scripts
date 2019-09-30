# developed by nchilaka
# this script writes to a file dst_file by seeking data from src_file at offset 0 and size of 1025 (ie to unalign with ec)
src_file = open("file", "r")
dst_file = open("dst_file", "a+")
for i in range(1000):
        src_file.seek(0, 0)
        dst_file.write(src_file.read(1025))
src_file.close()
dst_file.close()

