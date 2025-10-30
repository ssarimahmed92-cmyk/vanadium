from math import *
import matplotlib.pyplot as plt

x = [-180, -150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150, 180]
y = [cos(-180), cos(-150), cos(-120), cos(-90), cos(-60), cos(-30), cos(0),
     cos(30), cos(60), cos(90), cos(120), cos(150), cos(180)]

plt.plot(x, y, color="blue")
plt.show()