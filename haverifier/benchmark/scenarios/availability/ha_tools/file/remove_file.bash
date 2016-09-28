#!/bin/bash

# Create new file.
# parameter: $1 - file-name

if [ -e $1 ]; then
 rm $1
fi