####this program plots bunch of points in 3D space with points in different colors. 3dpoints_curve.txt has 3D points and
##hexstring.txt has color for each point.##
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import Image
import matplotlib.cm as cm
import numpy as np
import time
plt.ion() ### interactive plotting.
plt.show()
#ax = fig.add_subplot(111, projection='3d')
f=open("/home/iiith/Desktop/hex/3dpoints_dataset_side3_far_rotation0.txt", 'r') #3d points.
f1=open("/home/iiith/Desktop/hex/side_3_far.txt", 'r') #robot movement.
data=f.read()
data2=f1.read()
#print data
data= data.split('\n')
data2= data2.split('\n')
cord=[row.split(' ') for row in data2]
cord.pop()
p=[row[0] for row in cord]
p1=[float(x) for x in p]
q=[row[1] for row in cord]
q1=[float(x) for x in q]
r=[]
for x in range(0,len(p1)):
    r.append(0)
print p1, q1, r
X = [row.split(' ') for row in data]
X.pop()
x = [row[0] for row in X]

xs=[float(x) for x in x]

y=[row[1] for row in X]

ys=[float(x) for x in y]

z=[row[2] for row in X]

zs=[float(x) for x in z]

#print ys
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title("3D recostruction.")
f1=open("/home/iiith/Desktop/hex/color_dataset_side3_far_rotation0.txt", 'a+') ## color of 3D points in HEX 
data1=f1.read().splitlines()
ax.plot_wireframe(p1, q1, r)
#data1= data.split('\n')
#print data1
ax.scatter(xs, ys, zs,s=80, c=data1, marker='^')
ax.scatter( p1, q1,r,s=80, marker='>')
##################
ax2 = fig.add_subplot(551)
ax2.set_title("Query Image ")
ax3=fig.add_subplot(554)
ax3.set_title("Match1 ")
ax4=fig.add_subplot(555)
ax4.set_title("Match2")
for i in range(0,6):
    fname = '/home/iiith/Desktop/f0000'+str(i)+'.png'
    print i
    fname1 = '/home/iiith/Desktop/f0000'+str(i)+'.png'
    fname2 = '/home/iiith/Desktop/f0000'+str(i)+'.png'
    image = Image.open(fname).convert("L")
    image1 = Image.open(fname1).convert("L")
    image2 = Image.open(fname2).convert("L")
    arr = np.asarray(image)
    arr1 = np.asarray(image1)
    arr2 = np.asarray(image2)
    cax=ax2.imshow(arr, cmap = cm.Greys_r)
    cax=ax3.imshow(arr1, cmap = cm.Greys_r)
    cax=ax4.imshow(arr2, cmap = cm.Greys_r)
    plt.draw()
    time.sleep(1)
    
