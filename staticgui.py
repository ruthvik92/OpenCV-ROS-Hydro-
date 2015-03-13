"""
A simple example of an animated plot... In 3D!
"""
import numpy as np
import matplotlib.pyplot as plt
from  mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import Image
import matplotlib.cm as cm
fname = '/home/iiith/Desktop/f00000.png'
image = Image.open(fname).convert("L")
arr = np.asarray(image)
X1, Y1, Z1 = [20,30,20,20,50,10,70,80,60,100],[5,60,20,3,13,20,10,20,40,80],[20,30,30,30,50,70,9,11,10,010]
# Attaching 3D axis to the figure######subplot##############
fig = plt.figure()
ax = fig.add_subplot((111), projection='3d')
ax.set_xlabel('X-dir')
ax.set_ylabel('Y-dir')
ax.set_zlabel('Z-dir')
ax.set_title("Robot Position and Image feature points in 3D.")
ax.plot_wireframe(X1, Y1, Z1)
f1=open("/home/iiith/Desktop/python graphs/3dpoints_curve.txt", 'r')
data1=f1.read()
data1= data1.split('\n')
X = [row.split(' ') for row in data1]
X.pop()
x = [row[0] for row in X]
xs=[float(x) for x in x]
y=[row[1] for row in X]
ys=[float(x) for x in y]
z=[row[2] for row in X]
zs=[float(x) for x in z]
f2=open("/home/iiith/Desktop/python graphs/hexstring.txt", 'r')
data2=f2.read().splitlines()
ax.scatter(xs, ys, zs, c=data2, marker='^')
##################subplots##################
ax2 = fig.add_subplot(551)
ax2.set_title("Query Image ")
ax3=fig.add_subplot(555)
ax3.set_title("Closest Img-1 to query ")
ax3=fig.add_subplot(556)
ax3.set_title("Closest Img-1 to query")
cax=ax2.imshow(arr, cmap = cm.Greys_r)
#fig.colorbar(cax)
##ax2.plt.imshow(arr, cmap = cm.Greys_r)
plt.show()
