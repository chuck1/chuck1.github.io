
#awk '{print $1 $4}' /var/log/apache2/access.log | cut -d: -f1 | uniq -c
#awk '{print $1 $4}' /var/log/apache2/access.log | uniq -c
awk '{print $1 $4}' /var/log/apache2/access.log | sed 's/(.*)\[(.*)/$2 $1/'

