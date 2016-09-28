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
config_file=$2


bak=".bak"
if [ -e "$config_file$bak" ]; then
    echo 'the backup config file exist'
    cp -p "$config_file$bak" "$config_file"
#    chmod 666 $config_file
fi

service $service_name start
