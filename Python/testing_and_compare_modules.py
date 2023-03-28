"""
Page to testing modules, compare and discuss the results
"""

"""
Testing ssm_linear_knn_decisiontree module
"""

"""
Testing linear regression part
"""

import numpy as np
import ssm_linear_knn_decisiontree as ssmlkd
import time

x = 2 * np.random.rand(10000000,1)
y = 4 + 3 * x + np.random.rand(10000000,1) # Create testing values, estimate coeff is about k = 3, b = 4,5

time1 = time.time()
k, b = ssmlkd.SSMLinearRegression(x, y)
time2 = time.time()
print("Results of SSMLinearRegression")
print("Incline_coeff is:", k)
print("Shift_value is:  ", b)
print("Time of calculation", time2 - time1)

from sklearn.linear_model import LinearRegression

time3 = time.time()
model = LinearRegression()
model.fit(x, y)
time4 = time.time()
print("Results of sklearn LinearRegression")
print(f"Coef_: {model.coef_} \nIntercept_: {model.intercept_}")
print("Time of calculation", time4 - time3)

print("Time of SSM/ time of sklearn:", (time2 - time1)/(time4 - time3))

