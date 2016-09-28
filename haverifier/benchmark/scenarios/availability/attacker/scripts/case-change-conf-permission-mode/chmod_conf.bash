#!/bin/bash
##############################################################################
# Copyright (c) 2015 Huawei Technologies Co.,Ltd and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################

# remove the read permission for a config file

set -e

service_name=$1
config_file=$2

bak=".bak"
if [ -e "$config_file" ]; then
    echo 'removing the all of the permission of the configure file'
    chmod 000 $config_file
fi

service $service_name restart