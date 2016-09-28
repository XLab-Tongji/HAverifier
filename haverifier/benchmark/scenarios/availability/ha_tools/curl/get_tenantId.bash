#! bin/bash
#get tenant id

#parameters:  $1:client_name  $2:token

curl -g -i -X GET http://192.168.0.2:8774/v2/ -H "User-Agent: "$1 -H "Accept: application/json" -H "X-Auth-Token: {SHA1}"$2