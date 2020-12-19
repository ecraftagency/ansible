#!/bin/sh
# Generate hosts.init file
# Default will use private ip
#
###########################
if [ "$1" == "public" ]; then
    export TF_KEY_NAME=ipv4_address
else
    export TF_KEY_NAME=ipv4_address_private
fi
./do.sh --list | ./inventory_builder.py
