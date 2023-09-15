import matplotlib.pyplot as plt

categories=["A","B","C","D"]
values=[10,20,15,25]

color_codes=["#ff0000","#00ff00","#0000ff","gold"]
plt.figure(figsize=(8,6))
plt.bar(categories,values,color=color_codes)
plt.xlabel("categories")
plt.ylabel("values")
plt.title("bar plot with colors")
plt.show()