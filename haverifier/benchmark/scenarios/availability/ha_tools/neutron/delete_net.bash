#!/bin/bash
# delete a network
#parameters: $1 -network name
source ~/openrc
neutron net-delete $1
