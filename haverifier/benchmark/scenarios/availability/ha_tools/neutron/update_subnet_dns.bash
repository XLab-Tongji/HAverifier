#!/bin/bash
# update a subnet dns
#parameters: $1 -subnet name $2-dns address $3-dns address 
source ~/openrc
neutron subnet-update $1 --dns-nameservers $2 $3