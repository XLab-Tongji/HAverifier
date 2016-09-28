#!/bin/bash

##############################################################################
# Copyright (c) 2015 Huawei Technologies Co.,Ltd and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################

# this script Set a node to standby status.
# Usage:
#   standby [<node>] [<lifetime>]
#   lifetime :: reboot | forever
# The node parameter defaults to the node where the command is run.

crm node standby $@