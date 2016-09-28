#!/bin/bash

# delete image
# parameter: $1 - image name/ID.
source ~/openrc
nova image-delete $1