import pandas as pd 
import matplotlib.pyplot as plt
data = pd.read_csv("tips.csv")
plt.hist(data['total_bill'])
plt.title("histogram")
plt.show()