#!/bin/bash

##############################################################################
# Copyright (c) 2015 Huawei Technologies Co.,Ltd and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################

# this script will try to delete a the a container named 'test_container',it works if
# the swift-container service is ready, otherwise it will raise a 503 Server Error

set -e

source /root/openrc
swift delete test_container