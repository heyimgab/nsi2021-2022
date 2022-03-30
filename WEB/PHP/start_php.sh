#!/bin/sh
if [ $# -ne 2 ]; then 
    echo "$0 <port> <dir>"
    exit 10 
fi
/usr/sbin/apache2 -DFOREGROUND -d. -f.htaccess -C"PidFile `mktemp`" \ 
-C"Listen $1" -C"ErrorLog /dev/stdout" -C"DocumentRoot $2" -e debug