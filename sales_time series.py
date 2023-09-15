import pandas as pd 
import matplotlib.pyplot as plt

sales_df = pd.read_csv('/content/sales.csv', parse_dates=['shipdate_year'])

monthly_sales = sales_df.groupby(pd.Grouper(key='shipdate_year', freq='M'))['sales'].sum()


plt.plot(monthly_sales.index,monthly_sales.values)
plt.xlabel("month")
plt.ylabel("sales")
plt.title("yearly sales")
plt.show()