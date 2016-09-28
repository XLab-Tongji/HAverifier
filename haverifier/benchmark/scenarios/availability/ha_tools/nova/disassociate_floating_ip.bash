#!/bin/bash

# disassociate floating ip with instance
# parameters: $1 - instance name $2 - floating ip
source ~/openrc
nova floating-ip-disassociate $1 $2