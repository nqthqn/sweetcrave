import time
import serial
import sys
# ftdi drivers
# configure the serial connections (the parameters differs on the device you are connecting to)
# serial('com1','baudrate',19200,'databits',8,'terminator',13);
ser = serial.Serial(
  port=sys.argv[1], # /dev/tty.KeySerial1 ? /dev/tty.USA19H142P1.1 ?
  baudrate=19200, # 19200
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS
)

# 15mm 0.7ml  ? min... 5ml 4 times (5ml is about a mouthfull? )

if not ser.isOpen():
    ser.open()


print ser

# ser.write('buz1')
# time.sleep(1)

# commands = ['BUZ1', 'DIA26.59', 'BUZ1', 'PHN01', 'FUNRAT', 'RAT15MM', 'VOL0.7', 'DIRINF',
#             'PHN02', 'FUNRAT', 'RAT7.5MM', 'VOL.5', 'DIRINF', 'PHN03',
#             'FUNRAT', 'RAT15MM', 'VOL0.7', 'DIRWDR', 'PHN04', 'FUNSTP',
#             'DIA26.59', 'PHN01', 'FUNRAT', 'BUZ1', 'RAT15MM', 'VOL1.0', 'DIRINF',
#             'PHN02', 'FUNRAT', 'RAT7.5MM', 'VOL.5', 'DIRINF', 'PHN03',
#             'FUNRAT', 'RAT15MM', 'VOL1.0', 'DIRWDR', 'PHN04', 'FUNSTP']
commands = ['BUZ1', 'DIA26.59', 'BUZ1', 'PHN01', 'FUNRAT']
for cmd in commands:
    print cmd
    ser.write(cmd)
    time.sleep(1)
    out = ''
    while ser.inWaiting() > 0:
        out += ser.read(1)
    if out != '':
        print '>>' + out

# Dynamic
# print 'Enter your commands below.\r\nInsert "exit" to leave the application.'
# input = 1
# while 1:
#     input = raw_input(">> ")
#     if input == 'exit':
#         ser.close()
#         exit()
#     else:
#         # send the character to the device
#         # (note that I happend a \r\n carriage return and line feed to the
#         # characters - this is requested by my device)
#         ser.write(input)  # + '\r\n'
#         out = ''
#         # let's wait one second before reading output
#         # (let's give device time to answer)
#         time.sleep(1)
#     while ser.inWaiting() > 0:
#         out += ser.read(1)
#     if out != '':
#         print ">>" + out
