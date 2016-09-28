#!/bin/bash

##############################################################################
# Copyright (c) 2015 Huawei Technologies Co.,Ltd and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################

# this script delay the out flow packages of a interface in some seconds.
# Usage:
#   delay_interface_flow <interface> <seconds>
# parameter interface - the target network interface for example eth0.
# parameter seconds - time to delay for every out package, for example 100 means delay 100 ms.

tc qdisc add dev $1 root netem delay $2