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

#plt.show()



def Gen_RandLine(length, dims) :
    """
    Create a line using a random walk algorithm

    length is the number of points for the line.
    dims is the number of dimensions the line has.
    """
    lineData = np.empty((dims, length))
    ##print lineData
    lineData[:, 0] = np.random.randint(-450,400,dims)
    for index in range(1, length) :
        # scaling the random numbers by 0.1 so
        # movement is small compared to position.
        # subtraction by 0.5 is to change the range to [-0.5, 0.5]
        # to allow a line to move backwards.
        step = ((np.random.rand(dims) - 0.5) * 0.1)
        lineData[:, index] = lineData[:, index-1] + step

    return lineData

def update_lines(num, dataLines, lines) :
    for line, data in zip(lines, dataLines) :
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2,:num])
    return lines

# Attaching 3D axis to the figure######subplot##############
fig = plt.figure()
ax = fig.add_subplot((111), projection='3d')
ax.set_xlabel('X-dir')
ax.set_ylabel('Y-dir')
ax.set_zlabel('Z-dir')
ax.set_title("Robot Position and Image feature points in 3D.")
data = [Gen_RandLine(500, 3) for index in range(1)]
lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]
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
# Fifty lines of random 3-D lines
####################3Dlineplot############################
data2=f2.read().splitlines()

# Setting the axes properties
ax.scatter(xs, ys, zs, c=data2, marker='^')
# Creating fifty line objects.
# NOTE: Can't pass empty arrays into 3d version of plot()

# Creating the Animation object
line_ani = animation.FuncAnimation(fig, update_lines, 25, fargs=(data, lines),
                              interval=50, blit=False)
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
