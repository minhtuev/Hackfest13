# testing code sample for sending out serial commands from python to robot

import serial

ser = serial.Serial('/dev/tty.KeySerial1', 57600, timeout=1)

ser.write("128 131")
ser.flush()
ser.write("137 0 100 128 0")
ser.flush()

ser.close()