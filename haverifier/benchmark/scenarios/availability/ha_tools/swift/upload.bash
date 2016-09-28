#!/bin/bash

# upload file to swift
#parameters: $1:container name $2:upload file name
source /root/openrc
swift upload $1 $2