import socket
import pickle

s = socket.socket()
port = 12345
print("Port: " + str(port))

s.connect(("192.168.1.156", port))
val = ["foo", 42, True]
data = pickle.dumps(val)
print(data)
print("=-=-=-=-=-=-=-=-=")
s.send(data)
print(s.recv(1024))
s.close
