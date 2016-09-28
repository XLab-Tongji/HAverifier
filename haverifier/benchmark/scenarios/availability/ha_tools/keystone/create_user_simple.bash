#!/bin/bash

# create new user
# parameter: $1 - user name
source ~/openrc
keystone user-create --name $1 