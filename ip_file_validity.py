import os.path
import sys

#Checking IP address file and its content validity
def ip_file_validity():
    #Prompting user for input
    ipaddr_file = input("\n# Enter IP file path and name (e.g. D:\MyApps\myfile.txt): ")
    

    #Checking if file exist
    if os.path.isfile(ipaddr_file) == True:
        print("\n* IP file is valid. ")

    else:
        print("\n* File {} does not exit. Please check and try again. \n" .format(ipaddr_file))
        sys.exit()
    
    #Open user selected file for reading (IP address file)
    ip_file = open(ipaddr_file, "r")

    #Move cursor to the beggining
    ip_file.seek(0)

    #Reading user provided file and coverting it to a list
    ip_list = ip_file.readlines()

    #Closing the file
    ip_file.close()

    return ip_list  #returning IP list


