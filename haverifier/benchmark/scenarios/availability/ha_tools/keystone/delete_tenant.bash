#!/bin/bash

# delete tenant
# parameter: $1 - tenant;
source ~/openrc
keystone tenant-delete $1