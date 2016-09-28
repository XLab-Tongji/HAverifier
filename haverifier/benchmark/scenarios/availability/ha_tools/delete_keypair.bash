#!/bin/bash

# delete keypair 
# parameters: $1 - pub key name
source ~/openrc
nova keypair-delete $1