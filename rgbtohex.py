f = open('/home/iiith/Desktop/python graphs/color_curve.txt', 'r')
global lat
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb
for line in f.read().split('//n'):
    r,g,b=line.split('/s')
    ##lat= line.split('//s')
    print r
    print rgb_to_hex(float(lat[0]),float(lat[1]),float(lat[2]))

##thi converts the input file which has color codes in range of 0-255 to hex values.



 
