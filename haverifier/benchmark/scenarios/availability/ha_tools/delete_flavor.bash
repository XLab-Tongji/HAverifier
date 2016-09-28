#!/bin/bash

# delete a flavor
# parameter: $1 - flavor name/id.

set -e

source /root/openrc

nova flavor-delete $1