import serial

ser = serial.Serial("COM6", 115200, timeout=1000)

ser.close()
ser.open()

recieved = []
string = ''

while True:
    x = ser.read(2)

    if x:
        x = x.decode("utf-8")

        Data = open('Data.txt', 'w')
        Data.write(x)
        Data.close()

        print(x)
