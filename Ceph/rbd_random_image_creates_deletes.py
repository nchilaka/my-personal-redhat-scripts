'''
# for i in {1..10000};do echo "####### loop $i #####" |& tee -a imagecreation.log; date|& tee -a imagecreation.log; python image.py |& tee -a imagecreation.log;date |& tee -a imagecreation.log;done
# for i in {1..20000};do echo "#### loop $i ####" |& tee -a ceph-health-command.log;date |& tee -a ceph-health-command.log; ceph -s |& tee -a ceph-health-command.log;echo "=== rbd ls dockerpool1 ==" |& tee -a ceph-health-command.log;  rbd ls dockerpool1|wc -l |& tee -a ceph-health-command.log;echo "=== rados ls --pool  dockerpool1 |wc -l =="  |& tee -a ceph-health-command.log |& tee -a ceph-health-command.log; rados ls --pool dockerpool1 |wc -l |& tee -a ceph-health-command.log; echo "___rados df____"  |& tee -a ceph-health-command.log; rados df |& tee -a ceph-health-command.log;ceph df |& tee -a ceph-health-command.log;ceph osd df |& tee -a ceph-health-command.log;sleep 300;done
'''

import random, os, string
from time import sleep

# rbd shortened command
rbd = 'docker exec ceph-mon-zod rbd '


# Function to get current image list
def get_imagelist():
    list_image_cmd = rbd + 'ls dockerpool1'
    imagelist = list_of_ls = os.popen(list_image_cmd).read().split('\n')
    # print(imagelist)
    sleep(5)
    return imagelist[:-1]


# Creation of images
def create_image(imagecount):
    # print(len(imagesize))
    imagesize_list = [size for size in range(300) if size % 10 == 0]
    print("number of images being created in this loop is {}".format(imagecount))
    for i in range(imagecount):
        # Logic to create random image names
        chars = string.ascii_lowercase + string.digits
        imagename = ''.join(random.choice(chars) for _ in range(13))
        cmd = rbd + 'create dockerpool1/' + imagename + ' --size ' +\
              str(random.choice(imagesize_list)) + 'G'
        os.system(cmd)


def del_image(imagelist):
    print("inside del function {}".format(imagelist))
    imagelist1 = [ele for ele in imagelist if 'gluster' not in ele if
                  'image' not in ele]
    for ele in range(random.choice(range(len(imagelist1)))):
        cmd = rbd + ' rm dockerpool1/' + imagelist1[ele]
        os.system(cmd)
    


# random blocks of image creations and deletions
op = ['create', 'delete']
operation = random.choice(op)
print(operation)
if operation == 'create':
    currentimagelist = get_imagelist()
    count = 10000 - len(currentimagelist)
    create_image(random.choice(range(count)))
    newimagelist = get_imagelist()
    list_of_newly_created_images = set(newimagelist) - set(currentimagelist)
    print("the newly created images are \n {}".format(
        list_of_newly_created_images))

else:
    imagelist = get_imagelist()
    print("printing image list {}".format(imagelist))
    del_image(imagelist)
    get_imagelist()

cmd = rbd + ' ls dockerpool1 |wc -l'
print("number of images is: {}".format(os.popen(cmd).read()))

