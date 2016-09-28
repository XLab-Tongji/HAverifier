#!/bin/bash

# Create new file.
# parameter: $1 - file-name

echo "creating file: $1 ......."
if [ -e $1 ]; then
 rm $1
fi
touch $1