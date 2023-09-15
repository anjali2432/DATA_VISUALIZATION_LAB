import matplotlib.pyplot as plt
import numpy as np

x=np.random.normal(loc=0,scale=1,size=100)
y=np.random.normal(loc=0,scale=1,size=100)

plt.figure(figsize=(8,6))
plt.scatter(x,y,alpha=0.5,s=50,edgecolors="k",linewidths=1,c="blue",label="data")
plt.xlabel("x")
plt.ylabel("y")
plt.title("transparency")
plt.legend()
plt.show()