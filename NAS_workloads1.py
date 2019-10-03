"""
this script is supposed to do below:
1) check if the client is already in use by checking if another volume is already mounted
2) then mount the volume on this client using a random server hostname
3) ask user what all IOs needs to run
4) trigger those IOs
"""

import os, random, time

print('''
PRE-REQUISITES FOR THIS SCRIPT
1) Make sure the cluster is established
2) Identify all the clients and enter them into the LIST clients_list
3) PASSWORDLESS SSH from the node where script is running to ALL CLIENTS and SERVERS
4) screen and wget must be installed (or have the machines subscribed to)
5) For cleaner execution(very much recommended but not mandatory) follow additional set of below instructs:
    a) umount all the existing volumes if any on the clients
    b) rm -rf all the directories under /mnt which are not in use
    c) delete the logs in /var/log/glusterfs
''')
time.sleep(1)
tmp = input("do you want to proceed, type yes or no:\n")
if tmp != 'yes':
    print("Exiting as it seems you don't want to continue, as you didnt enter an yes\n")
    exit()

print("Proceeding with the script \n")
mngt_node = input("kindly enter one server node hostname and make sure it has passwordless ssh setup up:\n")
my_cmd = 'ssh root@' + mngt_node + ' gluster peer status'
# print(my_cmd)
peerstatus = os.popen(my_cmd).read()

my_cmd = 'ssh root@' + mngt_node + ' gluster v list'
tmp = os.popen(my_cmd).read()
vol_list = tmp.split("\n")
vol_list.pop()
print('list of volumes in the cluster are:', vol_list)


def mountlogic():
    print("will be mounting all the volumes on the cluster on this client \n:")
    for vol in vol_list:
        dir = 'ssh root@' + client + ' mkdir /mnt/' + vol
        os.popen(dir).read()
        mount = 'ssh root@' + client + ' mount -t glusterfs ' + random.choice(servers_list) + ':' + vol + ' /mnt/' + vol
        os.popen(mount).read()


if "Disconnected" in peerstatus:
    print("One or more nodes is in Disconnected state")
    exit()
# populating server hostnames from peer status
my_cmd = 'ssh root@' + mngt_node + ' gluster peer status|grep Hostname:|awk \'{print $2}\''
tmp = os.popen(my_cmd).read()
servers_list = tmp.split("\n")
servers_list.append(mngt_node)
print('list of SERVERS in the cluster are:', servers_list)
cond = ('yes', 'no', 'skip')

clients_list = ['10.70.43.21', '10.70.42.166', '10.70.35.113']
print('list of CLIENTS provided are:', clients_list)
for client in clients_list:
    print("WILL BE MOUNTING THE VOLUMES ON GIVEN CLIENTS \n")
    print("MAKE SURE PASSWD LESS ssh has been established from node where script is running to clients and servers \n")
    time.sleep(30)

    # checking if any volume is mounted at all
    if_mount = 'ssh root@' + client + ' mount|grep glusterfs'
    tmp = os.popen(if_mount).read()
    if "glusterfs" in tmp:
        print("Seems like there is already a volume mounted")
        inp = input("do you want to proceed? enter yes or no, or type 'skip' to go to next part:\n")
        while True:
            print(inp)
            if inp == 'no':
                exit()
            elif inp == 'skip':
                break
            elif inp not in cond:
                inp = input("please enter only yes or no:\n")
            else:
                print("golan")
                print("going ahead and mounting volume \n")
                mountlogic()
    else:
        print("going ahead and mounting volume \n")
        mountlogic()

# copy all scripts
'''
for server in servers_list:
    wget = 'ssh root@' + server + \
           ' wget http://rhsqe-repo.lab.eng.blr.redhat.com/sosreports/nchilaka/Scripts/Test_Scripts_Repo.tar.gz'
    os.system(wget)
'''


def clientside_io():
    print('''
    Will be starting below IOs on each of the mount point on each of the clients:
    # 1) untar the ClientSide_Test_Scripts_Repo.tar.gz test repo
    # 2) start capturing top o/p
    # 3) start kernel untar work load for {1..100}
    # 4) indefinite lookups using find *|xargs stat
    ''')
    for client in clients_list:
        wgetrepo = 'ssh root@' + client + \
               ' wget http://rhsqe-repo.lab.eng.blr.redhat.com/sosreports/nchilaka/Scripts/Test_Scripts_Repo.tar.gz'
        os.system(wgetrepo)
        #starting IO
        repountar = 'ssh root@' + client + ' tar -xvf Test_Scripts_Repo.tar.gz'
        os.system(repountar)
        chperm =  'ssh root@' + client + ' chmod -R 0777 Test_Scripts_Repo'
        os.system(chperm)
        execlauncher = 'ssh root@' + client + \
                       ' Test_Scripts_Repo/ClientSide_Test_Scripts_Repo/launcherscript_top_kerneluntar_lookups.sh'
        os.system(execlauncher)


clientside_io()


################## FUTURE pending workS ####################

'''
def top_output():
    tmp = input("if you want to capture top output of clients, servers, or both then enter clients, servers, both:\n")
    if tmp == 'clients':
        for client in clients_list:
            # ssh root@10.70.43.21 screen -d -m -S 'top' "./lookup.sh "
            # mkdir  /mnt/<vnames>/IO
            # mkdir /mnt/<vnames>/logs
            # mkdir /mnt/<vnames>/logs/top
            # scp /home/nchilaka/01_Scripts root@<client>:~
            # cp /home/nchilaka/01_Scripts/lookup.sh /mnt/<vname>/logs/

'''

# rhs-client6.lab.eng.blr.redhat.com
# check for gluster and rhel version