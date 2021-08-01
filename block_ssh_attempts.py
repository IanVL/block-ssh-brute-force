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
		#Create loop to repeat the following checks for each item in the list
		for string_var in split_line:
			#Save string in front of "port" (should be ip-address) in string_var
			string_var = split_line[split_line.index("port") - 1]
			#Check if string_var contains an IPv4 or IPv6 address
			if "????.????.????.????" or "????:????:????:????:????:????:????:????" in String_var:
				ip_address = string_var
			#Add ip_address to ip_dict if not present and add a count of 1
			if ip_address not in ip_dict:
				ip_dict[ip_address] = 1
			#If present add 1 to count
			else:
				ip_dict[ip_address] += 1
		
#Block ip address if count is 3 or more
for ip_address in ip_dict:
	#Retrieve count and check if equal to or greater then 3
	count = ip_dict[ip_address]
	if count >= 3:
		#Block the ip address via the function in the given module (fwblock)
		fwblock.block_ip(ip_address)
		#Print the blocked ip address to the terminal
		print(ip_address + " has been blocked.")
	#If no ip address is blocked print this to the terminal
	else:
		print("No ip address has been blocked")
		

