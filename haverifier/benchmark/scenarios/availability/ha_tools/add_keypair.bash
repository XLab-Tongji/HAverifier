#!/bin/bash

# add= keypair to the nova keypair list
# parameters: $1 - pub key name
source ~/openrc
nova keypair-add --pub-key  ~/.ssh/id_rsa.pub $1