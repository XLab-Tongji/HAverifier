#!/bin/bash

# delete service from Service Catalog.
# parameter: $1 - service;
source ~/openrc
keystone service-delete $1