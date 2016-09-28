#!/bin/bash

# create new user
# parameter: $1 - user name;$2(optional) - user password;$3 - tenant;$4 - true|false.
source ~/openrc
keystone user-create --name $1  --pass $2  --tenant $3 --email $4  --enabled $5