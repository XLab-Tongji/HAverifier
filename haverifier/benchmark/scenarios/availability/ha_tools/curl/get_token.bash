#! bin/bash
#get token from keystoen

curl -g -i -X GET http://192.168.0.2:5000/ -H "Accept: application/json" -H "User-Agent: python-keystoneclient"