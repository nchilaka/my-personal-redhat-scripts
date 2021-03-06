# Developed by nchilaka
'''
this test helps in creating volumes of different types and configs randomly
User needs to modify below variables:
1) enter the hostname to the "hosts" list. This is a list of gluster server nodes
2) subvols: change this to the number of bricks suffixes required. 
   Note that it takes brick path as /gluster/brick*
   hence, if there are /gluster/brick{1..10} then you can feed to this to use /gluster/brick{1..10}
3) ranvoltype you need to enter the type of volumes you need
4) Note that this script creates only 1 volume of a random type.
   To create, say 500, volumes, then just run it in a loop as below:
   for i in {1..500};do python <scriptname>;done
5) This script doesn't mount the volume(s) created
'''



import os, string, random

chars = string.ascii_lowercase + string.digits
random_string = ''.join(random.choice(chars) for _ in range(13))



hosts = ['dhcp35-75.lab.eng.blr.redhat.com', 'dhcp35-194.lab.eng.blr.redhat.com', 'dhcp35-173.lab.eng.blr.redhat.com', 'dhcp35-108.lab.eng.blr.redhat.com', 'dhcp35-42.lab.eng.blr.redhat.com', 'dhcp35-182.lab.eng.blr.redhat.com']


randomhost = random.choice(hosts)
subvols = (random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(randomhost)
#randvoltype = (random.choice(['disp', 'dist-disp', 'rep' , 'dist-rep', 'arb', 'dist-arb', 'single']))
randvoltype = (random.choice(['disp', 'rep' , 'arb', 'single']))
#randvoltype = 'dist-rep'
brick_selected = (random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))

if randvoltype == 'single':
	print("voltype selected is single")
	print("%s, %s" % (randvoltype, brick_selected))
	vname = randvoltype + '_' + random_string
	print(vname)
	brickpath = '/gluster/brick' + str(brick_selected) + '/' + vname
	print(brickpath)
	cmd =  "gluster v create %s %s:%s" % (vname, randomhost, brickpath)
	print(cmd)
	os.system(cmd)
	os.system('gluster v start %s' % vname)

elif randvoltype == 'disp':
	final_brickpath = " "
	print("voltype selected is %s" % randvoltype)
	print (randvoltype, brick_selected)
	vname = randvoltype + '_' + random_string
	print (vname)
	for i in hosts:
		host_brickpath = i + ':/gluster/brick' + str(brick_selected) + '/' + vname
		print(host_brickpath)
		final_brickpath = final_brickpath + host_brickpath + " "
	cmd =  "gluster v create %s disperse 6 redundancy 2 %s" % (vname, final_brickpath)
	print(cmd)
	os.system(cmd)
	os.system('gluster v start %s' % vname)

elif randvoltype == 'dist-disp':
	final_brickpath = " "        
	vname = randvoltype + '_' + random_string
	print("create a volume named %s of type %s with distribute count of %s "  %(vname, randvoltype, subvols))
	for r in range(1,subvols):
		for i in hosts:
			host_brickpath = i + ':/gluster/brick' +  str(r) + '/' + vname
			final_brickpath = final_brickpath + host_brickpath + " "
	print(final_brickpath)
	print(" ############################# ")
	cmd =  "gluster v create %s disperse 6 redundancy 2 %s" % (vname, final_brickpath)
	print(cmd)
	os.system(cmd)
	os.system('gluster v start %s' % vname)

elif randvoltype == 'rep' :
	final_brickpath = " "
	print("voltype selected is a PURE %s" % randvoltype)
	print(randvoltype, brick_selected)
	vname = randvoltype + '_' + random_string
	print (vname)
	for each in random.sample(hosts, 3) :
		host_brickpath = each + ':/gluster/brick' + str(brick_selected) + '/' + vname
		print(host_brickpath)
		final_brickpath = final_brickpath + host_brickpath + " "
	cmd =  "gluster v create %s rep 3 %s" % (vname, final_brickpath)
	print(cmd)
	os.system(cmd)
	os.system('gluster v start %s' % vname)

elif randvoltype == 'dist-rep':
	final_brickpath = " "
	vname = randvoltype + '_' + random_string
	print("create a volume named %s of type %s with distribute count of %s "  %(vname, randvoltype, subvols))
	for r in range(1,subvols):
		for each in random.sample(hosts, 3) :
			host_brickpath = each + ':/gluster/brick' + str(r) + '/' + vname
			final_brickpath = final_brickpath + host_brickpath + " "
	print(final_brickpath)
	print(" ############################# ")
	cmd =  "gluster v create %s rep 3 %s" % (vname, final_brickpath)
	print(cmd)
	os.system(cmd)
	os.system('gluster v start %s' % vname)

elif randvoltype == 'arb' :
	final_brickpath = " "
	print("voltype selected is a PURE %s" % randvoltype)
	print(randvoltype, brick_selected)
	vname = randvoltype + '_' + random_string
	print (vname)
	#for i in range(0,3) :
	for each in random.sample(hosts, 3) :
		host_brickpath = each + ':/gluster/brick' + str(brick_selected) + '/' + vname
		print(host_brickpath)
		final_brickpath = final_brickpath + host_brickpath + " "
	cmd =  "gluster v create %s rep 3 arbiter 1 %s" % (vname, final_brickpath)
	print(cmd)
	os.system(cmd)
	os.system('gluster v start %s' % vname)

elif randvoltype == 'dist-arb' :
	final_brickpath = " "
	final_brickpath = " "
	vname = randvoltype + '_' + random_string
	print("create a volume named %s of type %s with distribute count of %s "  %(vname, randvoltype, subvols))
	for r in range(1,subvols):
		#for i in range(0,3):
		for each in random.sample(hosts, 3):
			host_brickpath = each + ':/gluster/brick' + str(r) + '/' + vname
			final_brickpath = final_brickpath + host_brickpath + " "
	print(final_brickpath)
	print(" ############################# ")
	cmd =("gluster v create %s rep 3 arbiter 1 %s" % (vname, final_brickpath))
	print(cmd)
	os.system(cmd)
	os.system('gluster v start %s' % vname)
