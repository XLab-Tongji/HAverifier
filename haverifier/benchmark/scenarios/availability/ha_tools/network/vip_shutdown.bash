#!/bin/bash

##############################################################################
# Copyright (c) 2015 Huawei Technologies Co.,Ltd and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################

# this script put a resource in manage mode
# Usage:
#   vip_shutdown <rsc> <interface> [netns]
# parameter rsc - resource id setting in pacemaker
# parameter interface - vip interface
# parameter netns - network namespace

if [ $# -lt 2 ]; then
    echo 'Usage: vip_shutdown <rsc> <vip>'
    exit 2
else
    RESOURCE=$1
    INTERFACE=$2
    if [ $# -eq 3 ]; then
        NETNS=$3
    else
        NETNS='default'
    fi
fi

TARGETNODE=$(crm_resource --quiet --locate --resource $RESOURCE | sed -e '/(null)/d')
ssh $TARGETNODE "ip netns exec $NETNS ifconfig $INTERFACE down"
