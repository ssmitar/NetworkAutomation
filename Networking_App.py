import sys

from ip_file_validity import ip_file_validity
from Checking_ipaddr_validities import ip_addr_valid
from ping_reach_test import ip_ping
from SSH_Connection import ssh_connection
from create_threads import create_threads

#Saving the list of IP addresses in ip.txt to a variable
ip_list = ip_file_validity()

#Checking IP address for valid IP address
try:
    ip_addr_valid(ip_list)

except KeyboardInterrupt:
    print("\n\n Program aborted by user. Exiting....\n")
    sys.exit()

#Verifying reachability of IP addresses
try:
    ip_ping(ip_list)

except KeyboardInterrupt:
    print("\n\n Excecution was interruped by user. Exiting...\n")
    sys.exit()

#Creating a thread
create_threads(ip_list, ssh_connection)

#End of program