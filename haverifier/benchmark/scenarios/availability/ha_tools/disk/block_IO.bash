#!/bin/bash
#make a disk IO jam 


sudo dd if=/dev/zero of=/test.dbf bs=8k count=30000000 &