#!/usr/bin/python3

import sys
Debug = 0
Verbose = 0
Not_Blocking = 0
n = len(sys.argv)

g = n - 2
while g != 0:
    if sys.argv[g] == "-n":
        Not_Blocking = 1
    elif sys.argv[g] == "-d":
        Debug = 1
    elif sys.argv[g] == "-v":
        Verbose = 1
    elif sys.argv [g] == "-h":
        print("Usage: block_ssh_attempts.py [-h] [-v] [-d] [-n] textfile.txt\n\nDescription: Blocking attackers their ip from your firewall, who had invalid login 3 or more times\n\nOptional arguments:\n-h, help	 	shows this file\n-v, verbose	 	prints every blocked ip address to screen\n-d, Debug	 	Prints debug lines\n-n, not Blocking 	Doesn't block the ips, for testing purpose  \n\nNot Optional arguments:\ntextfile.txt		File you want to get used by the script \n\n\n")
    else:
        import sys
        print >> sys.stderr, "message"
    g = g -1

if sys.argv[-1] == "-h":
    print("Usage: block_ssh_attempts.py [-h] [-v] [-d] [-n] textfile.txt\n\nDescription: Blocking attackers their ip from your firewall, who had invalid login 3 or more times\n\nOptional arguments:\n-h, help	 	shows this file\n-v, verbose	 	prints every blocked ip address to screen\n-d, Debug	 	Prints debug lines\n-n, not Blocking 	Doesn't block the ips, for testing purpose  \n\nNot Optional arguments:\ntextfile.txt		File you want to get used by the script \n\n\n")

#opening the file which needs to be checked
if sys.argv[-1] != "-h":
    file_object  = open(sys.argv[-1], "r")

#Importing the firewall-blocking module with name fwblock
    import fwblock

    #Creating new Dictionary for saving IP's
    ip_dict = {}




    #line 14-15 detect which line has "Invalid user" in it
    for line in file_object:    
        if "Invalid user" in line:
            #line 16-18 splits up the line, and checks the word infront of the word port (which always is the IP address) then gives it the name Ip_adress
            split_line = line.split()
            word = split_line[split_line.index("port") - 1]
            if "." or ":" in word:
                ip_address = word
            #checks if IP is in dictionary if not adds it, if it is it changes it adds 1 to it's count
            if ip_address not in ip_dict:
                ip_dict[ip_address] = 1
            else:
                ip_dict[ip_address] += 1

    #checks if the ip has been used 3 times or more, if so it blocks the IP address.
    for ip_address in ip_dict:
        count = ip_dict[ip_address]
        if count >= 3:
            #blocking the Ip address
            if Not_Blocking == 0:
                
                if Debug == 1:
                    print("\nDEBUG: MODULE IS WORKING")

                #fwblock.block_ip(ip_address)
                if Verbose == 1:
                    print("blocking " + ip_address)
            
    #Closing the file
    file_object.close()


    if Debug == 1:
        print("\nTotal arguments passed:", n)
        print("\nName of Python script:", sys.argv[0])
        print("\nName Of File", sys.argv[-1])
        print(ip_dict)
