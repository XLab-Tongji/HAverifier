#!/bin/bash

# create volume using cinder
# parameters: $1 - volume name $2 - the size of volume (G)
source ~/openrc
cinder create --display_name $1 $2