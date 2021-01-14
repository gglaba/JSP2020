import numpy as np

x = np.matrix([[1,2,3,-2,-1],[3,5,5,-3,-9],[2,3,2,0,-8],[2,6,7,-5,1],[1,2,6,-4,-10]])
y = np.matrix([[6],[2],[-5],[17],[12]])
x_odw = np.linalg.inv(x)
z = x_odw * y
print(" x = " + str(z[0]) + "\n" + " y = " + str(z[1]) + "\n"  + " z = " + str(z[2]) + "\n" + " t = " + str(z[3]) + "\n" + " u = " + str(z[4]))
