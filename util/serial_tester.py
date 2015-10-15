import time
import serial

# configure the serial connections
# (the parameters differs on the device you are connecting to)
# /dev/tty.KeySerial1 ? /dev/tty.USA19H142P1.1 ?

ser = serial.Serial(port='/dev/tty.KeySerial1',
                    baudrate=19200,  # 19200
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )

if not ser.isOpen():
    ser.open()

print 'Enter your commands below.\r\nInsert "exit" to leave the application.'

input = 1
while True:

    input = raw_input(">> ")
    if input == 'exit':
        ser.close()
        exit()
    else:
        # send the character to the device
        # (note that I happend a \r\n carriage return and line feed
        # to the characters - this is requested by my device)
        ser.write(input + '\r\n')
        out = ''
        # let's wait one second before reading output
        # (let's give device time to answer)
        time.sleep(1)
        while ser.inWaiting() > 0:
            out += ser.read(1)

    if out != '':
        print ">>" + out
