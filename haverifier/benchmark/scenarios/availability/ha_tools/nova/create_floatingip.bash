#!/bin/bash

# create floating-ip
# parameter: $1(optional) - ip address
set -e

source /root/openrc

nova floating-ip-create $1