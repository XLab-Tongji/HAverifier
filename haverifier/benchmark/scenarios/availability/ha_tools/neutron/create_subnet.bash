#!/bin/bash
#create a new subnet
#parameters: $1 -network name ,the subnet belongs $2-CIDR of the subnet,eg:192.168.2.0/24 $3 subnet name(optinal) 
source ~/openrc
neutron subnet-create $1 $2 --name $3
