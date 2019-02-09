import paramiko
import os.path
import time 
import sys
import re

#Checking username and password file for authentication
#propmting user to input file destination or path 
cred_file = input("\n# Enter user file path and name. e.g.(D:\Myapps\myfile.txt): ")

#When credentials file is valid
if os.path.isfile(cred_file) == True:
    print("\n* Username file is valid. \n")

#When credentials file is not valid
else:
    print("\n* File {} does not exist. Please check and try again." .format(cred_file))
    sys.exit()

#Checking commands file
#Prompting user to input command file path and name
command_file = input("\n# Please enter name and path for command file. (e.g. D:\MyApps\myfile.txt): ")

#when command file is vaild
if os.path.isfile(command_file) == True:
    print("\n* Command file is valid. \n")

#When Command file is invalid
else:
    print("\n* Command file {} is not valid. Please check and try again. \n" .format(command_file))
    sys.exit()


#Opening up SSH connection
def ssh_connection(ip):
    global cred_file        #inportthing global variables inside the method
    global command_file     #importing global variables inside the method

    #Creating SSH connection
    try:
        #Define ssh parameters
        user_file = open(cred_file, "r")

        #Moving cursor back to the beggining
        user_file.seek(0)

        #Rading username from the file
        username = user_file.readlines()[0].split(",")[0].rstrip("\n")
        
        #Moving cursor back to the beggining of the file
        user_file.seek(0)

        #Reading password for file
        password = user_file.readlines()[0].split(",")[1].rstrip("\n")
        
        #Logging in remote device via SSH
        session = paramiko.SSHClient()

        #For testing purpose, following code allows auto-accepting unkown host keys
        #Do not use following in production envirnment because of security concerns
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #Connecting to device using username and password
        session.connect(ip.strip("\n"), username = username, password = password)
        
        #Start an interative shell session on the router
        connection = session.invoke_shell()     #invokes CLI from the switch after connection is established

        #Setting terminal length for entire output - disable pagination
        connection.send("enable \n")                #sending "enable" command using paramikos send()
        connection.send("Terminal length 0\n")      #sending "terminal length command" using paramiko's send()
        time.sleep(1)

        #Entering global config mode
        connection.send("\n")               #Moving cursor to the new line on switch's CLI
        connection.send("Config t \n")      #Seding command for configure terminal via send()
        time.sleep(1)

        #Open command file for reading
        commads = open(command_file, "r")

        #Moving cursor to the start of the file 
        commads.seek(0)

        #Sending each line of command to the CLI of switch via CLI
        for each_line in commads.readlines():
            connection.send(each_line + "\n")
            time.sleep(2)
        
        #closing selected file
        commads.close()

        #closing username/password file 
        user_file.close()

        #Checking commad output for IOS syntax error
        router_output = connection.recv(65535)

        #Catching any syntax error created by IOS while executing our commnads
        if re.search(b"% Invalid input", router_output):
            print("\n* There was at least one IOS syntax error on device {} :" .format(ip))
        
        #In case there were no syntax errors
        else: 
            print("\n DONE for the device {}.: " .format(ip))
        

        #Test for reading command output 
        print(re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", str(router_output)))

        #Closing session
        session.close()
    
    #Catching any exceptions
    except paramiko.AuthenticationException:
        print("\n* Invalid user name and password. \n Please check username and password configuration and try again.")
        print("\n Closing program. Bye!!")
