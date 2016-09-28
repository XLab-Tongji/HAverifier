#!/bin/bash

# Create new role.
# parameter: $1 - role-name
source ~/openrc
keystone role-create --name $1