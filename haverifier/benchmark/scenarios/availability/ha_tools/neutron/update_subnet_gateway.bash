#!/bin/bash
# update a subnet gateway
#parameters: $1 -subnet name $2 gateway ip address
source ~/openrc
neutron subnet-update $1 --gateway_ip=$2