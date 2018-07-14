#!/usr/bin/env python

# little script for sending messages and syncronising time with arduino

import serial
import serial.tools.list_ports
import time

def connect():                       # Finds a list of arduinos and connects to the first one listed
	arduino_ports = [
		p.device
		for p in serial.tools.list_ports.comports()
		if 'USB2' in p.description
	]

	if not arduino_ports:
		raise IOError("No Arduino found")
	if len(arduino_ports) > 1:
		warnings.warn('Multiple Arduinos found - using the first')
	global ser
	ser = serial.Serial(arduino_ports[0],baudrate=9600,timeout=2)
	time.sleep(2)
	
	
	print 'Arduino port selected: ' + arduino_ports[0]
	timestamp = 'T' + str(int(2*time.time()-time.mktime(time.gmtime())))  # sketchy way of syncronising times...
	print ser.write(timestamp+":")
	print 'time sent: ' + timestamp
	

def write(code):
        while ser.inWaiting():
                ser.readline()
	ser.write(code+":")
	data = ser.readline()
	while ser.inWaiting():
		ser.readline()
	return data
		
def read():
	return ser.readline()
	

	
