#!/bin/bash
#create a new network with specified provider
#parameters: $1 -network name $2 -local or other networktypes 

source ~/openrc
neutron net-create $1 --provider:network-type $2
