from math import *
import matplotlib.pyplot as plt

x = [-180, -150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150, 180]
y = [sin(-180), sin(-150), sin(-120), sin(-90), sin(-60), sin(-30), sin(0),
     sin(30), sin(60), sin(90), sin(120), sin(150), sin(180)]

plt.plot(x, y, color="red")
plt.show()