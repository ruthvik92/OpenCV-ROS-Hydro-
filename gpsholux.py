import os
import serial
def get_present_gps():
    ser=serial.Serial('/dev/ttyUSB0',4800)
    ser.open()
                    # open a file to write gps data
    f = open('/home/iiith/Desktop/gps1.txt', 'a+')
    data=ser.read(1024) # read 1024 bytes
    f.write(data) #write data into file
    f.flush() #flush from buffer into os buffer
         #ensure to write from os buffers(internal) into disk
    f = open('/home/iiith/Desktop/gps1.txt', 'a+')# fetch  the required file
    f1 = open('/home/iiith/Desktop/gps2.txt', 'a+')
    for line in f.read().split('\n'):
        if line.startswith('$GPGGA'):
            
            try:
                lat, _, lon= line.split(',')[2:5]
                lat=float(lat)
                lon=float(lon)
                
                print lat/100
                print lon/100
                a=[lat,lon]
                f1.write(lat+",")
                f1.flush()
                f1.write(lon+"\n")
                f1.flush()
                f1.close()

            except:
                pass

while True:
    get_present_gps()
    
