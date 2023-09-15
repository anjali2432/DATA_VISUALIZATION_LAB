import numpy as np
import matplotlib.pyplot as plt
from  scipy import stats

data=np.random.gamma(1,3,1000)
plt.hist(data,bins=50)
plt.title("Skewed Data Histogram")
plt.show()

skewness=stats.skew(data)
print("Skewness :",skewness)


log_data=np.log(data)
plt.hist(log_data,bins=50)
plt.title("Transformed Data Histogram")
plt.show()

log_skewness=stats.skew(log_data)
print("Log_Skewness :",log_skewness)
