from time import sleep
from myo import init, Hub, DeviceListener
init('myo_sdk/bin')

class Listener(DeviceListener):
    def on_connect(self, myo, timestamp, firmware_version):
        print("Connected!")
    def on_pose(self, myo, timestamp, pose):
        print(str(pose))
        print("+=+=+=+=")

#listener = DeviceListener()
hub = Hub()
hub.run(1000, Listener())

try:
  while True:
      sleep(0.5)
finally:
  hub.shutdown()  # !! crucial