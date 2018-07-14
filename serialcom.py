#! /usr/bin/python

import serial
import sys
import time

ser = serial.Serial()
ser.port = "/dev/ttyACM0"
ser.baudrate = 9600
ser.timeout=2
ser.setDTR(False)
ser.open()

time.sleep(3)

def serialsend(code):
    ser.write(code+":")
serialsend(sys.argv[1])

