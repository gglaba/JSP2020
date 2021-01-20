import numpy as np
import matplotlib.pyplot as plt

v0 = int(input("Wprowadź v0 [m/s]: "))
alfa = int(input("Wprowadź kąt [stopnie]: "))

v0x = v0 * np.cos(alfa * np.pi / 180)
v0y = v0 * np.sin(alfa * np.pi / 180)
g = 9.81
h = v0y**2/(2*g)
z = (2*(v0**2)*np.sin(alfa * np.pi / 180)*np.cos(alfa * np.pi / 180))/g
Tmax = (2*v0y) / g

vy = list()
T = list()
vx = list()
s = list()
Sy = list()

def danewykres():
    for i in np.arange(0, Tmax, 0.01):
        vy.append(v0y - (g*i))
        T.append(i)
        vx.append(v0x)
        s.append(v0x*i)
        Sy.append(v0y * i - (g*(i**2)) / 2)

fig, (ax1, ax2, ax3) = plt.subplots(3)

danewykres()
ax1.plot(T, vy) # wykres chwilowa pionowa
ax1.plot(T, vx) #wykres chwilowa pozioma
ax2.plot(s, T) #wykres położenia od czasu
ax3.plot(s, Sy) #tor rzutu 
plt.show()


print("Wysokość maksymalna: " + str(h) + " m")
print("zasięg: " + str(z) + " m")
print("Czas: " + str(Tmax) + " s")
