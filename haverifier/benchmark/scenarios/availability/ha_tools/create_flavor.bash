#!/bin/bash

# create flavor
# parameter: $1-name $2-id $3-ram $4-disk $5-vcpus

set -e

source /root/openrc

nova flavor-create $1 $2 $3 $4 $5
