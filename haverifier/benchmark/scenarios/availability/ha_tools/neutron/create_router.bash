#!/bin/bash
#create a new router
#parameters: $1 -router name
source ~/openrc
neutron router-create $1