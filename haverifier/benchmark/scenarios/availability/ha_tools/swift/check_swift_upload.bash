#!/bin/bash

##############################################################################
# Copyright (c) 2015 Huawei Technologies Co.,Ltd and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################

# this script will try to verify the swift status, which will be successfully response
# to the caller if the swift-proxy or swift-account service is available, otherwise,it
# will raise a 503 Server Error

set -e

source /root/openrc

swift list |grep test_container| wc -l|awk '{if($1>0){ print "swift delete test_container"|"/bin/bash"}}'
swift upload test_container /etc/swift/swift.conf