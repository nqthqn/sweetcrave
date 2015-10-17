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
ser.write('VOL ML\r')
ser.write('TRGFT\r')
ser.write('AL 0\r')
ser.write('PF 0\r')
ser.write('BP 1\r')
ser.write('BP 1\r')

# phases 1 - 4
ser.write('phn01\r')
ser.write('rat15mm\r')
ser.write('vol.2\r')
ser.write('dirinf\r')

ser.write('phn02\r')
ser.write('funrat\r')
ser.write('rat15mm\r')
ser.write('vol.75\r')
ser.write('dirinf\r')

ser.write('phn03\r')
ser.write('funrat\r')
ser.write('rat15mm\r')
ser.write('vol.5\r')
ser.write('dirwdr\r')

ser.write('phn04\r')
ser.write('funstp\r')

ser.write('run01\r')
ser.write('run02\r')
ser.write('run03\r')
ser.write('run04\r')
ser.write('run05\r')

