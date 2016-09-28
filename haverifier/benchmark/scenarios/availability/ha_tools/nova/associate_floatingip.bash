#!/bin/bash

# associate floating ip with instance 
# parameters: $1 - instance name $2 - floating ip 
source ~/openrc
nova floating-ip-associate $1 $2 