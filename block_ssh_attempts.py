#!/usr/bin/python3

print("Prohibits certain ip addresses from gaining access via ssh.")

file_object  = open("/home/Ian/os-scripting/block-ssh-brute-force/sshdlog", "r")

import fwblock

ip_dict = {}

for line in file_object:
    if "invalid user" in line:
        split_line = line.split()
        for thing in split_line:
            if "." in thing:
                ip_address = thing
                if ip_address not in ip_dict:
                    ip_dict[ip_address] = 1
                else:
                    ip_dict[ip_address] += 1

for ip_address in ip_dict:
    count = ip_dict[ip_address]
    if count >= 3:
        fwblock.block_ip(ip_address)
        print(ip_address + " has been blocked")
