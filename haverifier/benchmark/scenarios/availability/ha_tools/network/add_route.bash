#!/bin/bash

# add new routes.
# parameter: $1 - network-address;$2 - netmask; $3 - interface-name.
source ~/openrc
route add -net $1 net mask $2 dev $3