import pandas as pd
import seaborn as sns


df=pd.read_csv("/content/rainfall in india 1901-2015.csv")

sns.barplot(df)