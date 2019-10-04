for i in {2..1000};do 

for x in { dhcp35-75.lab.eng.blr.redhat.com dhcp35-194.lab.eng.blr.redhat.com dhcp35-173.lab.eng.blr.redhat.com dhcp35-108.lab.eng.blr.redhat.com dhcp35-42.lab.eng.blr.redhat.com };do ssh root@$x "rm -rf /gluster/brick{5..20}/ecv*" ;done

gluster v add-brick ecv  dhcp35-75.lab.eng.blr.redhat.com:/gluster/brick5/ecv-new-$i dhcp35-194.lab.eng.blr.redhat.com:/gluster/brick5/ecv-new-$i dhcp35-108.lab.eng.blr.redhat.com:/gluster/brick5/ecv-new-$i dhcp35-173.lab.eng.blr.redhat.com:/gluster/brick5/ecv-new-$i dhcp35-42.lab.eng.blr.redhat.com:/gluster/brick5/ecv-new-$i dhcp35-182.lab.eng.blr.redhat.com:/gluster/brick5/ecv-new-$i dhcp35-75.lab.eng.blr.redhat.com:/gluster/brick6/ecv-new-$i dhcp35-194.lab.eng.blr.redhat.com:/gluster/brick6/ecv-new-$i dhcp35-108.lab.eng.blr.redhat.com:/gluster/brick6/ecv-new-$i dhcp35-173.lab.eng.blr.redhat.com:/gluster/brick6/ecv-new-$i dhcp35-42.lab.eng.blr.redhat.com:/gluster/brick6/ecv-new-$i dhcp35-182.lab.eng.blr.redhat.com:/gluster/brick6/ecv-new-$i dhcp35-75.lab.eng.blr.redhat.com:/gluster/brick7/ecv-new-$i dhcp35-194.lab.eng.blr.redhat.com:/gluster/brick7/ecv-new-$i dhcp35-108.lab.eng.blr.redhat.com:/gluster/brick7/ecv-new-$i dhcp35-173.lab.eng.blr.redhat.com:/gluster/brick7/ecv-new-$i dhcp35-42.lab.eng.blr.redhat.com:/gluster/brick7/ecv-new-$i dhcp35-182.lab.eng.blr.redhat.com:/gluster/brick7/ecv-new-$i --mode=script 

sleep 300

gluster v remove-brick  ecv  dhcp35-75.lab.eng.blr.redhat.com:/gluster/brick5/ecv-new-$i dhcp35-194.lab.eng.blr.redhat.com:/gluster/brick5/ecv-new-$i dhcp35-108.lab.eng.blr.redhat.com:/gluster/brick5/ecv-new-$i dhcp35-173.lab.eng.blr.redhat.com:/gluster/brick5/ecv-new-$i dhcp35-42.lab.eng.blr.redhat.com:/gluster/brick5/ecv-new-$i dhcp35-182.lab.eng.blr.redhat.com:/gluster/brick5/ecv-new-$i dhcp35-75.lab.eng.blr.redhat.com:/gluster/brick6/ecv-new-$i dhcp35-194.lab.eng.blr.redhat.com:/gluster/brick6/ecv-new-$i dhcp35-108.lab.eng.blr.redhat.com:/gluster/brick6/ecv-new-$i dhcp35-173.lab.eng.blr.redhat.com:/gluster/brick6/ecv-new-$i dhcp35-42.lab.eng.blr.redhat.com:/gluster/brick6/ecv-new-$i dhcp35-182.lab.eng.blr.redhat.com:/gluster/brick6/ecv-new-$i dhcp35-75.lab.eng.blr.redhat.com:/gluster/brick7/ecv-new-$i dhcp35-194.lab.eng.blr.redhat.com:/gluster/brick7/ecv-new-$i dhcp35-108.lab.eng.blr.redhat.com:/gluster/brick7/ecv-new-$i dhcp35-173.lab.eng.blr.redhat.com:/gluster/brick7/ecv-new-$i dhcp35-42.lab.eng.blr.redhat.com:/gluster/brick7/ecv-new-$i dhcp35-182.lab.eng.blr.redhat.com:/gluster/brick7/ecv-new-$i start --mode=script

sleep 300

gluster v remove-brick  ecv  dhcp35-75.lab.eng.blr.redhat.com:/gluster/brick5/ecv-new-$i dhcp35-194.lab.eng.blr.redhat.com:/gluster/brick5/ecv-new-$i dhcp35-108.lab.eng.blr.redhat.com:/gluster/brick5/ecv-new-$i dhcp35-173.lab.eng.blr.redhat.com:/gluster/brick5/ecv-new-$i dhcp35-42.lab.eng.blr.redhat.com:/gluster/brick5/ecv-new-$i dhcp35-182.lab.eng.blr.redhat.com:/gluster/brick5/ecv-new-$i dhcp35-75.lab.eng.blr.redhat.com:/gluster/brick6/ecv-new-$i dhcp35-194.lab.eng.blr.redhat.com:/gluster/brick6/ecv-new-$i dhcp35-108.lab.eng.blr.redhat.com:/gluster/brick6/ecv-new-$i dhcp35-173.lab.eng.blr.redhat.com:/gluster/brick6/ecv-new-$i dhcp35-42.lab.eng.blr.redhat.com:/gluster/brick6/ecv-new-$i dhcp35-182.lab.eng.blr.redhat.com:/gluster/brick6/ecv-new-$i dhcp35-75.lab.eng.blr.redhat.com:/gluster/brick7/ecv-new-$i dhcp35-194.lab.eng.blr.redhat.com:/gluster/brick7/ecv-new-$i dhcp35-108.lab.eng.blr.redhat.com:/gluster/brick7/ecv-new-$i dhcp35-173.lab.eng.blr.redhat.com:/gluster/brick7/ecv-new-$i dhcp35-42.lab.eng.blr.redhat.com:/gluster/brick7/ecv-new-$i dhcp35-182.lab.eng.blr.redhat.com:/gluster/brick7/ecv-new-$i  commit --mode=script

sleep 60;

echo " ############## loop $i completed ####################"
date
done
