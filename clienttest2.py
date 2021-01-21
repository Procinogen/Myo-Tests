import socket
import pickle
from time import sleep
from myo import init, Hub, DeviceListener
init('myo_sdk/bin')

#Socket Stuff
s = socket.socket()
port = 12345
print("Port: " + str(port))
#Sending Data
s.connect(("192.168.1.156", port))

#Setting up Myo-python
class Listener(DeviceListener):
    def on_connect(self, myo, timestamp, firmware_version):
        print("Connected!")
    def on_pose(self, myo, timestamp, pose):
        val = str(pose)
        data = pickle.dumps(val)
        print(val)
        print("=-=-=-=-=-=-=-=-=")
        s.send(data)
        myo.vibrate("short")
		

hub = Hub()
hub.run(1000, Listener())

try:
  while True:
      sleep(0.5)
finally:
  hub.shutdown()  # !! crucial
  s.close #Also crucial