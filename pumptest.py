import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
  port='/dev/tty.USA19H142P1.1', # /dev/tty.KeySerial1 ?
  baudrate=19200,
  parity=serial.PARITY_ODD,
  stopbits=serial.STOPBITS_TWO,
  bytesize=serial.SEVENBITS
)




if not ser.isOpen():
  ser.open()

print ser
commands = ['dia26.59', 'phn01', 'funrat', 'rat15mm', 'vol0.7', 'dirinf',
            'phn02', 'funrat', 'rat7.5mm', 'vol.5', 'dirinf', 'phn03',
            'funrat', 'rat15mm', 'vol0.7', 'dirwdr', 'phn04', 'funstp',
            'dia26.59', 'phn01', 'funrat', 'rat15mm', 'vol1.0', 'dirinf',
            'phn02', 'funrat', 'rat7.5mm', 'vol.5', 'dirinf', 'phn03',
            'funrat', 'rat15mm', 'vol1.0', 'dirwdr', 'phn04', 'funstp']

for cmd in commands:
  print cmd
  ser.write(cmd + '\r\n')
  time.sleep(1)
  out = ''
  while ser.inWaiting() > 0:
    out += ser.read(1)
  if out != '':
    print '>>' + out

# print 'Enter your commands below.\r\nInsert "exit" to leave the application.'

# input=1
# while 1 :
#   input = raw_input(">> ")
#   if input == 'exit':
#     ser.close()
#     exit()
#   else:
#     # send the character to the device
#     # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
#     ser.write(input + '\r\n')
#     out = ''
#     # let's wait one second before reading output (let's give device time to answer)
#     time.sleep(1)
#     while ser.inWaiting() > 0:
#       out += ser.read(1)

#     if out != '':
#       print ">>" + out
