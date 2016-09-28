#!/bin/bash

##############################################################################
# Copyright (c) 2015 Huawei Technologies Co.,Ltd and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################

# this script used to check node status, online or offline
# Usage:
#   node_status_assert <hostname> [online|offline]
# parameter hostname - hostname of target node

online=$( crm status | grep "Online" )
if [[ $online =~ $1 ]]; then
    if [[ 'online' == $2 ]]; then
        exit 0
    else
        exit 1
    fi
else
    if [[ 'offline' == $2 ]]; then
        exit 0
    else
        exit 2
    fi
fi