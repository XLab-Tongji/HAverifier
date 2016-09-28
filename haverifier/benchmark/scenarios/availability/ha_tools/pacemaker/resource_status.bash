#!/bin/bash

##############################################################################
# Copyright (c) 2015 Huawei Technologies Co.,Ltd and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################

# this script print resource status.More than one resource can be shown at once.
# If the resource parameter is left out, the status of all resources is printed.
# It can also check a resource status and then return zero meaning running and number
# greater than zero represents has stopped.
# Usage:
#   resource_status [<rsc> ...]
#   resource_status <rsc> --isRunning

hasOption=$( echo $@ | grep "isRunning")

if [[ "$hasOption" != "" ]]
then
    crm resource status $1 | grep running && return 0
    return 1
else
    crm resource status $@
fi
