import sys
import subprocess

#Checking switch availablity by a ping command
def ip_ping(list):

    for ip in list:
        ip = ip.rstrip("\n")    #rstrip strips right most specified character from the list. In this case "\n"

        #using subprocess call method we are pinging givin IP address two times
        ping_reply = subprocess.call("ping %s /n 2" %(ip), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
        #if ping is successful
        if ping_reply == 0:
            print("\n {} is reachable \n" .format(ip))
            continue
    
        #if ping is not successful
        else:
            print("\n* {} is not reachable. Please check connectivity and try again. \n" .format(ip))
            sys.exit()

