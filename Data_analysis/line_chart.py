import pandas as pd 
import matplotlib.pyplot as plt
data = pd.read_csv("tips.csv")
plt.plot(data["tip"])
plt.plot(data["size"])
plt.xlabel("tip")
plt.ylabel("size")
plt.show()
