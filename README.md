# NetworkAutomation
Basic Network Automation using Python

Goal of this project is to get a command from an user, feed it to Python script, which will then SSH into a switch, run those provided commnand and filter IP addresses from the output generated on Switch's terminal. This project constains following contentsa are essential.

1) Arista EOS running in Virtual Environment (using Virtual Box). For this project 3 Virtual machines were used. One can add as many as they want. 
2) Switch is pre-configured with username, password and management IP in order to intiate SSH session. 
3) Finally a Python script which will automate the task. 

Python scripts does following:
1) There are three text files which were feed into the scipt. One file containing management IP addresses of all virtual switches. Second one containing username and password exactly same as configured on all switches. And finally, any commands which an user wants to perform. In this case "show ip loopback interface 0"(loopback interfaces were configured for this on switches) was used as an expamle. 
2) Script will take these files and will check if files exists in the first place or not. If they exists, IP address file will checked for valid IP addresses.
3) Before SSH session attempt is made, script will check if switches are reachable or not via ping test. 
4) Username and password will be crosscheck with username and password provided on the file. 
5) Finally, script will produce an output a list containing all the IP addresses that were in an terminal output.

