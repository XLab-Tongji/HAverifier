#!/bin/bash
#imitate a status of disk space full
# parameter: $1 -the space write per count,$2 - count

sudo dd if=/dev/zero of=/mnt/test bs=1G count=20 