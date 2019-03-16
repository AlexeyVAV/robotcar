import serial

ser = serial.Serial(
    port='/dev/ttyUSB0',\
    baudrate=19200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
    timeout=0)

print("connected to: " + ser.portstr)
count=1
line = []

while True:
    for c in ser.read():
        line.append(c)
        if c == '\n':
            #print(str(count) + str(': ') + chr(line) )
            print(str(count) + " : " +''.join(line))
            line = []
            count = count + 1
            break

ser.close()