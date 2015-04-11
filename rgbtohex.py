def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

with open('/home/iiith/Desktop/color_dataset_side3_far_rotation0.txt', 'r') as v:
    for line in v:
        if ' ' in line:
            a = line.strip().split(' ')
            a=rgb_to_hex((float(a[0]), float(a[1]), float(a[2]))) #arguement is a touple of 3 elements.
            print a
            f = open('/home/iiith/Desktop/hex/color_dataset_side3_far_rotation0.txt', 'a+')
            print a
            f.writelines(a+'\n')
            f.flush()
            
                
            
##this code converts color code from rgb to hex 
