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
