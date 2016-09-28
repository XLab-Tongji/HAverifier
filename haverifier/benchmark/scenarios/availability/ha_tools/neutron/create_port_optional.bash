#!/bin/bash
# create a port for a network with optional parameter
#parameters: $1 -network name $2 an ip address for the port which is optinal
source ~/openrc
neutron port-create $1 --fixed-ip ip_address=$2