#!/bin/bash

# remove volume using cinder
# parameters: $1 - volume name
source ~/openrc
cinder delete $1 