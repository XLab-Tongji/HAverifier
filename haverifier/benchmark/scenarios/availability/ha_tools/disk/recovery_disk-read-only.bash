#!/bin/bash
# recovery status from disk read only-restart the host
sudo echo "b" >/proc/sysrq-trigger
