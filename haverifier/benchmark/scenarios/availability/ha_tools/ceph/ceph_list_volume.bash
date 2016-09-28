#!/bin/bash

# list all the volumes in ceph
source ~/openrc
rados -p volumes ls