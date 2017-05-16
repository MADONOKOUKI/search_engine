import numpy as np
from scipy import stats

a = np.array([20.5, 5.3, 12.4, 2.9, 12.3, 6.7, 2.1, 13.1])
b = np.array([2.4, 16.1, 21.0, 10.9, 20.6, 25.7, 24.2, 18.0])

res = stats.ttest_ind(a, b)
print(res)