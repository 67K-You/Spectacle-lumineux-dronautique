import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import sys
from scipy import interpolate

x = [0.0]
y = [0.0]
z = [0.0]


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([-5.0,5.0])
ax.set_ylim([-5.0,5.0])
plt.plot(x[0], y[0], 'X')

def onclick(event):
    global x,y,z
    len_x = len(x)
    last_x = x[-1]
    last_y = y[-1]
    
    x+= [event.xdata]
    y+= [event.ydata]
    plt.plot(event.xdata, event.ydata, '.')
    fig.canvas.draw()
    z+= [float(input("Altitude: "))]
    plt.plot([last_x, event.xdata], [last_y, event.ydata], color=[0,0,z[-1]/10])
    fig.canvas.draw()
    
    
cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()

x+=[0.0]
y+=[0.0]
z+=[0.0]


## Ici on a récupéré les points
lineTime = 3.0
numLines = len(x)
t = np.linspace(0.0, numLines*lineTime, numLines)

Y3D = np.c_[x,y,z]
cs = interpolate.CubicSpline(t, Y3D)

file = open("traj.csv", "w")
file.write("duration,x^0,x^1,x^2,x^3,x^4,x^5,x^6,x^7,y^0,y^1,y^2,y^3,y^4,y^5,y^6,y^7,z^0,z^1,z^2,z^3,z^4,z^5,z^6,z^7,yaw^0,yaw^1,yaw^2,yaw^3,yaw^4,yaw^5,yaw^6,yaw^7,\n")
nlines = len(cs.c[0])
for i in range(nlines):
    print(nlines)
    file.write(str(lineTime) + "," + str(cs.c[3][i][0]) + "," + str(cs.c[2][i][0]) + "," + str(cs.c[1][i][0]) + "," + str(cs.c[0][i][0]) + "," + "0,0,0,0," +
               str(cs.c[3][i][1]) + "," + str(cs.c[2][i][1]) + "," + str(cs.c[1][i][1]) + "," + str(cs.c[0][i][1]) + "," + "0,0,0,0," +
               str(cs.c[3][i][2]) + "," + str(cs.c[2][i][2]) + "," + str(cs.c[1][i][2]) + "," + str(cs.c[0][i][2]) + "," + "0,0,0,0," +
               "0,0,0,0,0,0,0,0,\n")
file.close()

##Pourquoi pas plotter en 3D le rendu


## Ecrire le script python
file = open("traj_test.py", "w")
file.write("from pycrazyswarm import Crazyswarm\nimport uav_trajectory\n\n\n\n")
file.write("def main():\n")
file.write("    swarm = Crazyswarm()\n")
file.write("    timeHelper = swarm.timeHelper\n")
file.write("    cf1 = swarm.allcfs.crazyflies[0]\n\n")
file.write("    trajectory = uav_trajectory.Trajectory()\n")
file.write("    trajectory.loadcsv('traj.csv')\n")
file.write("    cf1.uploadTrajectory(1,0,trajectory)\n")
file.write("    cf1.startTrajectory(1)\n\n")
file.write("    timeHelper.sleep(" + str(numLines*lineTime) + ")\n\n\n\n")
file.write("if __name__ == '__main__':\n")
file.write("    main()\n")
file.close()
