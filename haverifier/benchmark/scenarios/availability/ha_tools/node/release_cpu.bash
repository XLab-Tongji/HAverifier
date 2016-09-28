#!/bin/bash
# release CPU stress.

ps -ef|grep "dd if=/dev/zero of=/dev/null"|awk '{print$2}'|xargs kill -9