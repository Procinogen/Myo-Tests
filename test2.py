import myo as myolib
from myo import init, Hub, DeviceListener, StreamEmg
import time
myolib.init('myo_sdk/bin')

class Listener(myolib.DeviceListener):
	def on_connect(self, myo, timestamp, firmware_version):
		myo.set_stream_emg(StreamEmg.enabled)
	def on_emg_data(self, myo, timestamp, emg):
		print(emg)

hub = myolib.Hub()
hub.run(1000, Listener())

try:
	while True:
		time.sleep(0.5)
except KeyboardInterrupt:
	print('\nQuit')
finally:
	hub.shutdown()