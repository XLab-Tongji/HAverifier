#!/bin/bash

##############################################################################
# Copyright (c) 2015 Huawei Technologies Co.,Ltd and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################

# this script reorder the out flow packages of a interface at a certain probability.
# Usage:
#   reorder_package <interface> <delay_time> <probability>
# parameter interface - the target network interface for example eth0.
# parameter delay_time - time to delay for every out package, for example 100 means delay 100 ms.
# parameter probability - the corrupt probability, for example 1% means corrupt packages at 1% probability.
# For example:
#       reorder_package eth0 10ms 25%
#   It will make 25% packages of eth0 send immediately and the others will delay 10ms.

tc qdisc add dev $1 root netem corrupt $2