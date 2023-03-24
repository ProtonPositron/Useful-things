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

x = 2 * np.random.rand(100,1) 
y = 4 + 3 * x + np.random.rand(100,1) # Create testing values, estimate coeff is about k = 3, b = 4,5

k, b = ssmlkd.SSMLinearRegression(x, y)
print("Incline_coeff is: ", k)
print("Shift_value is:", b)
