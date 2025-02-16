#!/bin/python3


import sys
import socket
from datetime import datetime as dt



#Define Target
if len(sys.argv) == 2:
    target=socket.gethostbyname(sys.argv[1])
    print("-"*20)
    print("Scanning Target: "+target)
    print("Time Started: "+ str(dt.now()))
    print("-"*20)
else:
    print("Invalid ammount of arguments")
    print("Syntax: python3 port_scanner.py <ip>")


try:
    for port in range(50,85):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print(f"port {port} is open")
        s.close()
        
        
        
except KeyboardInterrupt:
    print("\n Exiting Proram")
    sys.exit()
    
    
        
except socket.gaierror:
    print("\n Hostname couldn't be resolve")
    sys.exit()
    
    
        
except socket.error:
    print("\n Could not connect to server")
    sys.exit()
    
    
    
    
