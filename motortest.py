# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 10:45:32 2018

@author: Gerard
"""
#Setup stuff
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(True)

Input1 = 16
Input2 = 18
EnableMotor = 22

GPIO.setup(Input1, GPIO.OUT)
GPIO.setup(Input2, GPIO.OUT)
GPIO.setup(EnableMotor, GPIO.OUT)

#The juicy stuff
def Fpulse(in1, in2, en1):
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(en1,GPIO.HIGH)
    return

for x in range(0, 10):
    print("rotating!")
    Fpulse(Input1, Input2, EnableMotor)
    time.sleep(0.2)

GPIO.cleanup()