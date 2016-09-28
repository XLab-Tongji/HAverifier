#!/bin/bash

# stop instance/server
# parameter: $1 - server name/ID
source ~/openrc
nova stop $1