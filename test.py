# -*- coding: utf-8 -*-
"""
Created on Mon May  7 22:41:56 2018

@author: Gerard
"""
import myo as libmyo
libmyo.init('myo_sdk/bin')
feed = libmyo.device_listener.Feed()
hub = libmyo.Hub()
hub.run(1000, feed)
try:
    myo = feed.wait_for_single_device(timeout=10.0)  # seconds
    if not myo:
       print("No Myo connected after 10 seconds.")
       sys.exit()

    while hub.running and myo.connected:
        quat = myo.orientation
        print("Orientation:", quat.x, quat.y, quat.z, quat.w)
except KeyboardInterrupt:
    print("Quitting...")
finally:
    hub.shutdown()