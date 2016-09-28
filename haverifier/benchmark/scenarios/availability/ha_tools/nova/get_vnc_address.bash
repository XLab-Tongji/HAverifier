#!/bin/bash

# get the vnc address of instance

#parameters: $1 - instance name

source /root/openrc

nova get-vnc-console $1 novnc