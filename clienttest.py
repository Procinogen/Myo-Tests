# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 21:53:00 2018

@author: Gerard
"""
import socket
import pickle

s = socket.socket()
port = 12345
print("Port: " + str(port))

s.connect(("192.168.1.156", port))
val = ["foo", 20, True]
data = pickle.dumps(val)
s.send(data)
print(s.recv(1024))
s.close
