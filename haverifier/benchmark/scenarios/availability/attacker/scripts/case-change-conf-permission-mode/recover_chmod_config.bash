#!/bin/bash
##############################################################################
# Copyright (c) 2015 Huawei Technologies Co.,Ltd and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################

# Remove a config file

set -e

service_name=$1

bak=".bak"
echo "start adding the read and write permission for the config file"
config_file=$2
if [ -e "$config_file" ]; then
     chmod 666 $config_file
fi

echo "underlying service to be started is $service_name"
service $service_name start