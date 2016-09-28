#!/bin/bash

# this script ping a ip address and the default timeout is one second.
# Usage:
#   ping <ip> [timeout]
# parameter ip - ip address
# timeout - Specify a timeout, in seconds, before ping exits regardless of
# how many packets have been sent or received.

if [[ $# == 2 ]]; then
    TIMEOUT=$2
else
    TIMEOUT=1
fi
ping $1 -c 1 -w $TIMEOUT