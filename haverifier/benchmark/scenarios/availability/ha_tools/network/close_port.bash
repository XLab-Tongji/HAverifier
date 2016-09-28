#!/bin/bash

# close a certain port.
# parameter: $1 - port-numbers;

iptables -A INPUT -p tcp --dport $1 -j DROP