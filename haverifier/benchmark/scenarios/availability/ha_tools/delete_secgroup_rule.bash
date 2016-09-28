#!/bin/bash

# delete rules from a security group
# parameters: $1 - group name/id; $2 - protocol name; $3 - start port; $4 -stop port; $5 - CIDR.
source ~/openrc
nova secgroup-delete-rule $1 $2 $3 $4 $5