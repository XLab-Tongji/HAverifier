#!/bin/bash

# download file from swift
#parameters: $1:container name $2:download file name
source /root/openrc
if [ -e $2 ]
then
 rm $2
fi

swift download $1 $2