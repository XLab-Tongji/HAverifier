#! bin/bash
#image list

#parameters   $1:tenant_id    $2:client_name   $3:token

curl -g -i -X GET http://192.168.0.2:8774/v2/$1/images/detail -H "User-Agent: "$2 -H "Accept: application/json" -H "X-Auth-Token: {SHA1}"$3