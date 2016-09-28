#!/bin/bash

#kill all of the sub-processes

set -e

service_name=$1

echo "killing the main process..."

ps -ef|grep $service_name|awk '{if($3==1)print $2}'|xargs kill -9





