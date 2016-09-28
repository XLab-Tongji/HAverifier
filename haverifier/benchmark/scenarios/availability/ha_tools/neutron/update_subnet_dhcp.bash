#!/bin/bash
# update a subnet dhcp
#parameters: $1 -subnet name $2 --enable-dhcp or --disable-dhcp
source ~/openrc
neutron subnet-update $1 $2 