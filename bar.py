import pandas as pd
import seaborn as sns


df=pd.read_csv("/content/business-financial-data-september-2022-quarter.csv")

sns.barplot(df,x="Period",y="Data_value")