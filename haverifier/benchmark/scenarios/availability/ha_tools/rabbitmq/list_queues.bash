#!/bin/bash

##############################################################################
# Copyright (c) 2015 Huawei Technologies Co.,Ltd and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################

# This script returns queue details including information as follows.
# name - The name of the queue with non-ASCII characters escaped as in C.
# durable - Whether or not the queue survives server restarts.
# policy - Policy name applying to the queue.
# messages - Sum of ready and unacknowledged messages (queue depth).
# consumers - Number of consumers.
# state - The state of the queue. Normally 'running', but may be "{syncing, MsgCount}"
#         if the queue is synchronising. Queues which are located on cluster nodes that
#         are currently down will be shown with a status of 'down' (and most other
#         queueinfoitems will be unavailable).

rabbitmqctl list_queues name durable policy messages consumers state