#!/bin/bash

# delete user
# parameter: $1 - user;
source ~/openrc
keystone user-delete $1