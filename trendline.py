import pandas as pd
import seaborn as sns

df=pd.read_csv("/content/Automobile.csv")

sns. regplot(x=df["length"],y=df["mileage"],data=df)