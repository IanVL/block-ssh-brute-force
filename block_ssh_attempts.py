#!/usr/bin/python3

#Import modules
import argparse
import sys
import fwblock #Firewall blocking module

#Define the description (dsc)
def dsc(name=None):
	return "Description:\nBlock attackers ip address upon 3 or more failed login attempts."

#Define file help message (file_msg)
def file_msg(name=None):
	return "Open logfile containing login attempts"

#Define verbose help message (verbose_msg)
def verbose_msg(name=None):
	return "Increase output verbosity, print each ip address that will be blocked to the terminal"

#Define not_blocking help message (nb_msg)
def nb_msg(name=None):
	return "Don't call block_ip(). Can be used for test purposes in combination with -v: shows which ip addresses would be blocked if -n was not parsed"

#Initialize ArgumentParser()
parser = argparse.ArgumentParser(description=dsc())

#Add positional argument file
parser.add_argument("file", help=file_msg(), type=str)

#Add optional argument -v (--verbose)
parser.add_argument("-v", "--verbose", action="store_true", help=verbose_msg())

#add optional argument -n (--not_blocking)
parser.add_argument("-n", "--not_blocking", action="store_true", help=nb_msg())

#Define args
args = parser.parse_args()

#Open file containig login attempts
file_object = open(args.file, "r")

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
			if "???.???.???.???" or "????:????:????:????:????:????:????:????" in string_var:
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
		if not args.not_blocking:
			fwblock.block_ip(ip_address)
		#Print the blocked ip address to the terminal
		if args.verbose:
			print("Blocking " + ip_address)
