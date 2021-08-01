#!/usr/bin/python3

#Import modules
import sys
import fwblock #Firewall blocking module

#Open file containig login attempts
file_object = open("sshdlog", "r")

#Create ip dictionary
ip_dict = {}

#Search for "Invalid user" in file
for line in file_object:
	if "Invalid user" in line:
		#Split up the line
		split_line = line.split()
		#Save string in front of "port" (should be ip-address) in string_var
		string_var = split_line[split_line("port") - 1]
		#Check if string_var contains an IPv4 or IPv6 address
		if "????.????.????.????" or "????:????:????:????:????:????:????:????" in String_var:
		ip_address = string_var
		#Add ip_address to ip_dict if not present
		if ip_address not in ip_dict:
			ip_dict[ip_address] = 1
		#If present add 1 to count
		else:
			ip_dict[ip_address] += 1
		

		

