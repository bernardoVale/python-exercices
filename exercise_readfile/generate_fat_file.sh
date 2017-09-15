#!/bin/bash

cat fixtures/01.log >> aux_01.log
for (( ; ; ))
do
    cat aux_01.log >> big-file.log
    FILESIZE=$(wc -c <"big-file.log")
    echo $FILESIZE
    if [ $FILESIZE -ge 2157760122 ] ;then
      break
    fi
    cat big-file.log >> aux_01.log
done
rm aux_01.log
