#!/bin/bash

# Add role and tenant for a user
# parameter: $1 - user name $2 - role name $3 - tenant name
source ~/openrc
keystone user-role-add --user $1 --role $2 --tenant $3
