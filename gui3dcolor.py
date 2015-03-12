from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

import numpy as np
ax = fig.add_subplot(111, projection='3d')
f=open("/home/iiith/Desktop/python graphs/3dpoints_curve.txt", 'r') 
data=f.read()
#print data
data= data.split('\n')
X = [row.split(' ') for row in data]
X.pop()
x = [row[0] for row in X]

xs=[float(x) for x in x]

y=[row[1] for row in X]

ys=[float(x) for x in y]

z=[row[2] for row in X]

zs=[float(x) for x in z]

#print xs
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
f1=open("/home/iiith/Desktop/python graphs/hexstring.txt", 'r')
data1=f1.read().splitlines()
#data1= data.split('\n')
print data1
ax.scatter(xs, ys, zs, c=data1, marker='^')
plt.show()
