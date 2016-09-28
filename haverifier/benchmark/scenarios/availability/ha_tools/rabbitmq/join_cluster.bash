#!/bin/bash

##############################################################################
# Copyright (c) 2015 Huawei Technologies Co.,Ltd and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################

# Instruct the node to become a member of the cluster that the specified node is in.
# Before clustering, the node is reset, so be careful when using this command.
# For this command to succeed the RabbitMQ application must have been stopped, e.g. with stop_app.
# The origin cmd format is as follow.
#       join_cluster {clusternode} [--ram]
# clusternode - Node to cluster with.
# [--ram] - If provided, the node will join the cluster as a RAM node.

rabbitmqctl join_cluster $@