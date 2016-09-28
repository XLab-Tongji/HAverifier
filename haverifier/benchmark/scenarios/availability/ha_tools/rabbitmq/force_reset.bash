#!/bin/bash

##############################################################################
# Copyright (c) 2015 Huawei Technologies Co.,Ltd and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################

# This script return a RabbitMQ node to its virgin state.
# Removes the node from any cluster it belongs to, removes all data from the management database,
# such as configured users and vhosts, and deletes all persistent messages.

rabbitmqctl force_reset