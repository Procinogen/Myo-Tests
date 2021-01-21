# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 21:43:20 2018

@author: Gerard
"""
import socket
import pickle

s = socket.socket()
#host = socket.gethostname()
#print("Hostname: " + str(host))
port = 12345
print("Port: " + str(port))
s.bind(('', port))

s.listen(5)
while True:
    c, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    print(pickle.loads(c.recv(1024)))
    c.send('Thank you for connecting')
    c.close()                # Close the connection
