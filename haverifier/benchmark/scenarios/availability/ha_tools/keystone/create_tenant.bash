#!/bin/bash

# Create new tenant.
# parameter: $1 - tenant-name;$2(optional) - tenant-description;$3(optional)- true|false
source ~/openrc
keystone tenant-create --name $1  --description $2  --enabled $3