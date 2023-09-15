import pandas as pd
import seaborn as sns



df=pd.read_csv("C:\Users\patel\Downloads\Housing.csv")



sns.scatterplot(x="area",y="price",data=df,hue=df["mainroad"])