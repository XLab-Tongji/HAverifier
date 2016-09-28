#!/bin/bash
# query ports of network with specific ip address
#parameters: $1 -ip address you want to query
source ~/openrc
neutron port-list --fixed-ips ip_address=$1

