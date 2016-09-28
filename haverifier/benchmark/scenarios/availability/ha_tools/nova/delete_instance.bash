#!/bin/bash

# delete an instance/server
# parameter: $1 - instance name/id.

set -e

source /root/openrc

nova delete $1