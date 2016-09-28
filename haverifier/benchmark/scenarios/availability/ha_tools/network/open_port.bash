#!/bin/bash

# open a certain port.
# parameter: $1 - port-numbers;

iptables -A INPUT -p tcp --dport $1 -j ACCEPT