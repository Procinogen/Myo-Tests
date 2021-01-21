import socket
import pickle

s = socket.socket()
#host = socket.gethostname()
#print("Hostname: " + str(host))
port = 12345
print("Port: " + str(port))
s.bind(('', port))

s.listen(5)
try:
    while True:
    	c, addr = s.accept()     # Establish connection with client.
    	print('Got connection from', addr)
    	while True:
            print(pickle.loads(c.recv(1024)))
finally:
   c.close()                # Close the connection
