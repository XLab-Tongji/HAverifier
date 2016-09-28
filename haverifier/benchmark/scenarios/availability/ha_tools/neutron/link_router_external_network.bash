#!/bin/bash
# Link the router to the external provider network
#parameters: $1 -router name $2 external network name (admin-floating_net)
source ~/openrc
neutron router-gateway-set $1 $2