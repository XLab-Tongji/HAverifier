#!/bin/bash

# delete swift container
#parameters: $1:container name
source /root/openrc
swift delete $1