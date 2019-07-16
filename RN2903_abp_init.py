"""RN2903 on ABP LoRa Wan Confi6 iguration"""
"""Authors: Rubens Fernandes and Arlley Gabriel Diaz"""
"""Date: 16/07/2019"""

import serial
import json
import time

""" Set serial communication parameters """
port = "/dev/ttyACM0"
baudrate = 57600
timeout = 5
parity = "N"
stopbits = 1
bytesize = 8
""" ----------------------------------- """

ser = serial.Serial(port,baudrate,bytesize,parity,stopbits,timeout) #Init serial communication

if ser.isOpen() == False: #Checking if the serial port was oppened
	ser.open()

""" Getting the RN2903 firmware version """
print('command: sys get ver')
ser.write(b'sys get ver\r\n')
print(str(ser.readline()))
""" ----------------------------------- """

""" Getting the Device EUI to register in a LoRa Server application  """
print('command: sys get hweui')
ser.write(b'sys get hweui\r\n')
print(str(ser.readline()))
""" ---------------------------------------------------------------- """

""" Getting and setting the Data Rate in module, that defines the SF, BW and bit rate """
print('command (get): mac get dr')
ser.write(b'mac get dr\r\n')
print(str(ser.readline()))
dr = raw_input("Set the data rate value: ")
print('command (set): mac set dr %s' % (dr))
ser.write(b'mac set dr %s\r\n' % (dr))
print(str(ser.readline()))
ser.write(b'mac get dr\r\n')
print(str(ser.readline()))
""" --------------------------------------------------------------------------------- """

""" Setting the channel 0 data rate range from 0 to 3, according to LoRa WAN protocol specification"""
ch_drrange = raw_input("Set the channel to modify data rate range: ")
print('command: mac set ch drrange %s 0 3' % (ch_drrange))
ser.write(b'mac set ch drrange %s 0 3\r\n' % (ch_drrange))
print(str(ser.readline()))
""" ------------------------------------------------ """

""" Setting the next power transmission, according to RN2903 specification """
pwr = raw_input("Set the power transmission: ")
print('command: mac set pwridx %s' % (pwr))
ser.write(b'mac set pwridx %s\r\n' % (pwr))
print(str(ser.readline()))
""" ---------------------------------------------------------------------------- """

""" Setting device address in abp LoRa network """
devaddr = raw_input("Set the device address: ")
print('command: mac set devaddr %s' % (devaddr))
ser.write(b'mac set devaddr %s\r\n' % (devaddr))
print(str(ser.readline()))
""" ------------------------------------------ """

""" Setting device network session key in abp LoRa network """
nwkskey = raw_input("Set the device network session key: ")
print('command: mac set nwkskey %s' % (nwkskey))
ser.write(b'mac set nwkskey %s\r\n' % (nwkskey))
print(str(ser.readline()))
""" ------------------------------------------------------ """

""" Setting device application session key in ABP LoRa network """
appskey = raw_input("Set the device application session key: ")
print('command: mac set appskey %s' % (appskey))
ser.write(b'mac set appskey %s\r\n' % (appskey))
print(str(ser.readline()))
""" ---------------------------------------------------------- """

""" Setting only one channel to communicate with a single channel gateway (CH 0 - 902.3 MHz) """
for x in range (1, 72):
	print('command: mac set ch status %s off' % str(x))
	ser.write(b'mac set ch status %s off\r\n' % str(x))
	print(str(ser.readline()))
print('command: mac set ch status 0 on')
ser.write(b'mac set ch status 0 on\r\n')
print(str(ser.readline()))
""" ---------------------------------------------------------------------------------------- """

""" Save LoRa Wan settings and specifications on RN2903' EEPROM """
print('command: mac save')
ser.write(b'mac save\r\n')
print(str(ser.readline()))
""" ----------------------------------------------------------- """

""" Join module on ABP configuration """
print('command: mac join abp')
ser.write(b'mac join abp\r\n')
print(str(ser.readline()))
""" -------------------------------- """

ser.close()
