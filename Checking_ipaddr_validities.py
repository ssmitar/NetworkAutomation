import sys

#Checking IP addresses for validity and to check if they aren't reserved IPs

def ip_addr_valid(list):

    for ip in list:
        ip = ip.rstrip("\n")
        octet_list = ip.split(".")

        #Checking each IP against reserved IP addresses. i.e Length should be 4, first octet should be less than 223 and not 127
        # First octet and 2nd octet should not be equal to 169 or 254 repectively
        # And all other octets should have value less than 255
        if (len(octet_list) == 4) and (1<= int(octet_list[0]) <= 223) and (int(octet_list[0]) != 127) and (int(octet_list[0]) != 169 or int(octet_list[1]) != 254) and (int(octet_list[1]) <= 255) and (int(octet_list[2]) <= 255) and (int(octet_list[3]) <= 255):
            continue
        
        # if above conditions doesn't match
        else:
            print("\n* There was an invalid IP address in the file: {} \n" .format(ip))
            sys.exit()
    


