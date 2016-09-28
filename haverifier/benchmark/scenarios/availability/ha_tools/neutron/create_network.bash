#!/bin/bash
#create a new network
#$parameters: $1 -network name
source ~/openrc
neutron net-create $1