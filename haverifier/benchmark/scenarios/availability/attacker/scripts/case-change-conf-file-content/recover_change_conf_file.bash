#!/bin/bash

set -e

conf_file=$1
echo "copy the backup file ${conf_file}.bak back to ${conf_file}"
echo "recovering..."
cp "${conf_file}.bak" "$conf_file"
#chmod 666 "${conf_file}"
