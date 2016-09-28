#!/bin/bash

# delete routes.
# parameter: $1 - network-address;$2 - netmask; $3 - interface-name.

route del -net $1 net mask $2 dev $3