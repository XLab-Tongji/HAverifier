#!/bin/bash

set -e

match_content_start_with=$1 #content to match
replace_contentline_with=$2 #content to replace
conf_file=$3

echo "start changing the config file"

cp "$conf_file" "${conf_file}.bak"
chmod 666 "${conf_file}.bak"

sed -ie "s/$match_content_start_with/$replace_contentline_with/g" $conf_file

#nova-manage db sync

#sed -ie "/^$match_content_start_with/d" $conf_file
