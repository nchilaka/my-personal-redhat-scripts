# Ref:  1625961 - Writes taking very long time leading to system hogging 
# Ref: 1591208 - Writes taking very long time leading to system hogging 
# open a file, keep writing to the file with overlapping writes infinitely
# While the above was going on I did a reboot(or killed a brick) of n1(ie client-c0)
# after that I saw different abnormalities such as below:
# 1)doing ls -l from another mount was taking very long time even for displaying 10 files
# 2) gluster v heal info was not responding even after 5min(only one file needs to be healed)
# 3) fuse client process (glusterfs) from where the perl script was run had consumed 5.5GB memory
# 4)file size on the backend were all different on each of the 1x3 bricks

#!/usr/bin/perl
$offset=0;
#$len=2;
#while($offset<1000)
#open( $h, '>>', "$ARGV[0]" ) or die $!;
open( $h, '>', "$ARGV[0]" ) or die $!;

while(1)
{
#open( $h, '>>', "$ARGV[0]" ) or die $!;  #opening file for write in append mode, filename is fed at cli argument

seek( $h, $offset, 1 );

#print $h "offset:$offset \n ";
print $h "offset:$offset ";
#$offset=$offset + 20;
$offset=$offset + 1;

}
