import time
import serial

ser = serial.Serial(
                    port='com1',
                    baudrate=19200,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                   )
if not ser.isOpen():
    ser.open()

# sanity check
ser.write('BUZ13\r')
time.sleep(1)

# setup (1.7 seconds)
ser.write('DIA26.59\r')
time.sleep(.25)
ser.write('VOL ML\r')
time.sleep(.25)
ser.write('TRGFT\r')
time.sleep(.25)
ser.write('AL 0\r')
time.sleep(.25)
ser.write('PF 0\r')
time.sleep(.25)
ser.write('BP 1\r')
time.sleep(.25)
ser.write('BP 1\r')
time.sleep(.25)

# phases 1 - 4
ser.write('phn01\r')
time.sleep(.25)
ser.write('rat15mm\r')
time.sleep(.25)
ser.write('vol.2\r')
time.sleep(.25)
ser.write('dirinf\r')
time.sleep(.25)

ser.write('phn02\r')
time.sleep(.25)
ser.write('funrat\r')
time.sleep(.25)
ser.write('rat15mm\r')
time.sleep(.25)
ser.write('vol.75\r')
time.sleep(.25)
ser.write('dirinf\r')
time.sleep(.25)

ser.write('phn03\r')
time.sleep(.25)
ser.write('funrat\r')
time.sleep(.25)
ser.write('rat15mm\r')
time.sleep(.25)
ser.write('vol.5\r')
time.sleep(.25)
ser.write('dirwdr\r')
time.sleep(.25)

ser.write('phn04\r')
time.sleep(.25)
ser.write('funstp\r')
time.sleep(.25)

ser.write('run\r')
time.sleep(.25)

