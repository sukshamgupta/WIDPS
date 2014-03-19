#!/usr/bin/env python
import os
import warnings
import sys
warnings.filterwarnings('ignore')
import colorama
import time
import filter
from colorama import Fore, Back, Style
colorama.init()
##############################################################################################################
int_check=os.popen("ifconfig mon0").read()                 #Checking the Existence of Monitor Interface
##############################################################################################################
if not "error" in int_check:                               #if error in the returned value,start the interface
	start="airmon-ng start wlan0"                 	   #Starting the Interface
        run_int=os.popen(start).read()                     #Reading the output of the above command
        print("Starting Montior Mode Interface")           #Status Message
##############################################################################################################
else:
	print("Monitor Mode Present")                      #If Already Present then print a status message
##############################################################################################################
if(sys.argv[1]=="wifi" and sys.argv[2]=="auth"):	   #Command Line Argument for Ecrypted Mode
##############################################################################################################
	filter.auth()


