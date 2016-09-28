#!/bin/bash

# start instance/server
# parameter: $1 - server name/ID
source ~/openrc
nova start $1