#!/bin/bash

# Add service to Service Catalog.
# parameter: $1 - Service type;$2(optional) - name;$3(optional)- service-description
source ~/openrc
keystone service-create --type $1  --name $2  --description $3