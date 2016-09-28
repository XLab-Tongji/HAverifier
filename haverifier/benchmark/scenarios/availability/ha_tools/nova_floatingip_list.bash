#!/bin/bash

# list the floating ip 
# parameter: $1 - instance name/id.

set -e

source /root/openrc

nova floating-ip-list