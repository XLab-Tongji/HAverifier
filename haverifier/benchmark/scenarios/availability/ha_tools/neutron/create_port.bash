#!/bin/bash
# create a port for a network
#parameters: $1 -network name 
source ~/openrc
neutron port-create $1 