import socket
import pickle

s = socket.socket()
#host = socket.gethostname()
#print("Hostname: " + str(host))
port = 12345
print("Port: " + str(port))
s.bind(('', port))

#-=+=-=+motor stuff+=-=+=-

#Setup stuff
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(True)


#The juicy stuff
def Fpulse(in1, in2, en1, delay):
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(en1,GPIO.HIGH)
    print("rotating!")
    time.sleep(delay)
    return

s.listen(5)
while True:
    c, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    while True:
    	GPIO.setmode(GPIO.BOARD)
    	pose = pickle.loads(c.recv(1024))
    	Input1 = 16
    	Input2 = 18
    	EnableMotor = 22

    	GPIO.setup(Input1,GPIO.OUT)
    	GPIO.setup(Input2,GPIO.OUT)
    	GPIO.setup(EnableMotor,GPIO.OUT)

    	print(pose)
    	if(pose == "<Pose: fingers_spread>"):
    		Fpulse(Input1, Input2, EnableMotor, 0.2)
    	elif(pose == "<Pose: fist>"):
    		Fpulse(Input2, Input1, EnableMotor, 0.2)
    	else:
    		GPIO.cleanup()
c.close()                # Close the connection
