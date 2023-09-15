import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA



plt.scatter(sales_df["sales"],sales_df["profit"])
plt.xlabel("sales")
plt.ylabel("profit")
plt.title("sales vs profit")
plt.show()

pca=PCA(n_components=2)
sales_reduction=pca.fit_transform(sales_df[["sales","profit"]])
 

plt.scatter(sales_reduction[:,0],sales_reduction[:,1])
plt.xlabel("pc1")
plt.ylabel("pc2")
plt.title("reduced sales data")
plt.show()