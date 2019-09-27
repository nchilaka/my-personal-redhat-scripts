#this script creates about 1000 files if not existing and after that opens fd for each of these files
# it then appends the current time to the file and then we sleep for the said time
# post that we close fds of all the files
#intention is to check what happens if there are lot of fds open and during the sleep time we perform some actions like brickdown, rebalance etc

import time
from datetime import datetime

l = [] 
for i in range(1000):
	filename = 'nile' + str(i)
	print(filename)
	#fh = 'f' + str(i)
	l.append('f' + str(i))
	#print(fh)
        l[i] = open(filename, "a+")
        #time.sleep(2)
	timenow = datetime.now()
	print(timenow)
	l[i].write(str(timenow))
	l[i].write("\n")

print("###################  sleeping before closing all FDs ########## \n")	 		
time.sleep(60)
for x  in range(1000):
	l[x].close()

