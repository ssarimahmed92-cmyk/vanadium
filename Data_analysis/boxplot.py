import pandas as pd 
import matplotlib.pyplot as plt
data = pd.read_csv("tips.csv")
plt.boxplot(data['total_bill'])
plt.title("boxplot")
plt.show()