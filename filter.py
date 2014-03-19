#!/usr/bin/env python
import os                  	
def auth():
	print("[*]Authentication Finder Running")
        com="tshark -i mon0 -R wlan.fc.type_subtype==0x0B -T fields -E separator='==>' -e wlan.sa -e wlan.da"
        yo=os.system(com)
	print yo
