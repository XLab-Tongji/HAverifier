#!/bin/bash

# create instance from image.  
# parameters: $1 - flavor name/id; $2 - image name/id; $3 - netid; $4 -instance name.

set -e

source /root/openrc

nova boot --flavor $1 --image $2 --nic net-id=$3 $4