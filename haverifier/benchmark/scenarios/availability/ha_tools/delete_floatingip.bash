#!/bin/bash

# delete floatingip
# parameter: $1 - IP address.
set -e

source /root/openrc

nova floating-ip-delete $1