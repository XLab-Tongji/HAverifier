#!/bin/bash
# Link the router to the subnet
#parameters: $1 -router name $2 subnet name
source ~/openrc
neutron router-interface-add $1 $2