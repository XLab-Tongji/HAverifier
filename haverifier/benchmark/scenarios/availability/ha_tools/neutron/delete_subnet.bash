#!/bin/bash
# delete a subnet
#parameters: $1 -subnet name
source ~/openrc
neutron subnet-delete $1
