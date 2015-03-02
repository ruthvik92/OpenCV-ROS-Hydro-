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
    lineData[:, 0] = np.random.rand(dims)
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

# Attaching 3D axis to the figure
fig = plt.figure()
ax = fig.add_subplot((111), projection='3d')
ax2 = fig.add_subplot(551)
ax2.set_title("Query Image ")
ax3=fig.add_subplot(555)
ax3.set_title("Nearest Image-1 match found to the Query Image ")
ax3=fig.add_subplot(556)
ax3.set_title("Nearest Image-2 match found to the Query Image")
cax=ax2.imshow(arr, cmap = cm.Greys_r)
#fig.colorbar(cax)
##ax2.plt.imshow(arr, cmap = cm.Greys_r)
# Fifty lines of random 3-D lines
data = [Gen_RandLine(25, 3) for index in range(3)]

# Creating fifty line objects.
# NOTE: Can't pass empty arrays into 3d version of plot()
lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]

# Setting the axes properties
ax.set_xlim3d([0.0, 1.0])
ax.set_xlabel('X')

ax.set_ylim3d([0.0, 1.0])
ax.set_ylabel('Y')

ax.set_zlim3d([0.0, 1.0])
ax.set_zlabel('Z')

ax.set_title("Robot Position and Image feature points in 3D.")

# Creating the Animation object
line_ani = animation.FuncAnimation(fig, update_lines, 25, fargs=(data, lines),
                              interval=50, blit=False)

plt.show()
