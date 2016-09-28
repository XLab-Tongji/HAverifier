#!/bin/bash

##############################################################################
# Copyright (c) 2015 Huawei Technologies Co.,Ltd and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################

# This script returns exchange details including information as follows.
# name - The name of the exchange with non-ASCII characters escaped as in C.
# type - The exchange type (such as [direct, topic, headers, fanout]).
# durable - Whether or not the exchange survives server restarts.
# arguments - Exchange arguments.
# policy - Policy name for applying to the exchange.

rabbitmqctl list_exchanges name type durable arguments policy