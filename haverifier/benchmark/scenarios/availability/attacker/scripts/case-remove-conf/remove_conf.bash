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
echo "underlying service to be stopped is $service_name"
bak=".bak"
echo "starting removing config file"
config_file=$2
if [ -e "$config_file" ]; then
    echo 'the config file exist'
    cp -p "$config_file" "$config_file$bak"
    if [ $? -eq 0 ] ; then
        rm $config_file
    fi
fi
service $service_name restart
