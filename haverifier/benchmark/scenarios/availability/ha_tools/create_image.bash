#!/bin/bash

# create an image/snapshot for an instance/server.
# parameters: $1 - server name/id; $2 - image name.
source ~/openrc
nova image-create $1 $2