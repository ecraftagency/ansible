#!/usr/bin/env python3

# Converts Ansible dynamic inventory sources to static files
# Input is received via stdin from the dynamic inventory file
#   ex:
#     ec2.py --list | ansible-dynamic-inventory-converter.py

import json
import os
import sys
import re

ORIGIN_INVENTORY = "./inventory.ini"

# def add_vars(_type, _id, variables):
#     assert _type == "group" or _type == "host"
#     dir_name = "./%s_vars" % _type
#     if not os.path.isdir(dir_name):
#         os.mkdir(dir_name)
#     with open('%s/%s' % (dir_name, _id), 'a') as fh:
#         fh.write(pyaml.dump(variables))

# def add_host_vars(host, variables):
#     add_vars('host', host, variables)

# def add_group_vars(group, variables):
#     add_vars('group', group, variables)

def main():
    raw_json = sys.stdin.read()
    inventory = json.loads(raw_json)
    inventory_filename = "./hosts.ini"
    prepend_content = ""
    with open(ORIGIN_INVENTORY, 'r') as f:
        prepend_content=  f.read()

    with open(inventory_filename, 'w') as fh:
        fh.write(";;;;; USER DEFINED INVENTORY\n")
        fh.write(prepend_content+"\n")
        fh.write(";;;;; GENERATED INVENTORY \n")
        
        for group in inventory:
            if "hosts" in inventory[group]:
                fh.write("[%s]\n" % group)
                for host in sorted(inventory[group]["hosts"]):
                    fh.write("%s\n" % host)
                fh.write("\n")
            if "children" in inventory[group]:
                fh.write("[%s:children]\n" % group)
                for child in sorted(inventory[group]["children"]):
                    fh.write("%s\n" % child)
                fh.write("\n")
            if isinstance(inventory[group], list):
                fh.write("[%s]\n" % group)
                for host in sorted(inventory[group]):
                    fh.write("%s\n" % host)
                fh.write("\n")            

if __name__ == '__main__':
    main()

