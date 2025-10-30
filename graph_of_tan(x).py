from math import *
import matplotlib.pyplot as plt

x = [-180, -150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150, 180]
y = [tan(-180), tan(-150), tan(-120), tan(-90), tan(-60), tan(-30), tan(0),
     tan(30), tan(60), tan(90), tan(120), tan(150), tan(180)]
print(y)
plt.plot(x, y, color="green")
plt.show()