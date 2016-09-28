#!/bin/bash

# delete role
# parameter: $1 - role;
source ~/openrc
keystone role-delete $1