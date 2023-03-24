"""
    Some useful functions for Linear Regression, K Nearest Neighbours and Decision Tree methods
"""
# Author: Sergei Starkov

import numpy as np

def SSMLinearRegression (x, y = None):
    """
    Simplest linear regression function for one feature and one target data row using Least Squares method.
    Work with NumPy arrays. As input values is used two one-dimensional arrays or one two-dimensional array.

    INPUT:

        - x: one-dimensional array of arguments or two-dimensional array of arguments and values
        - y: one-dimensional array of values or None if x is two-dimensional

    OUTPUT:

          if equation like y = k * x + b then:
        - incline_coeff: k
        - shift_value: b
    """
    if x.ndim <= 2:
          if x.ndim == 2:
              if x.shape[0] > 2 and x.shape[1] > 2:
                  raise ValueError("number of rows or columns is more than two") 
              elif x.shape[0] == 2: # Modify two-dimension array in two one-dimension arrays
                  y = x[1,:]
                  x = x[0,:]
              elif x.shape[1] == 2:
                  y = x[:,1]
                  x = x[:,0]
              sxy = 0 # Define temporary parameters
              sx = 0
              sy = 0
              sxx = 0
              n = len(x)
              for i in range(0, n): # Construct one cicle for minimum processing
                  sxy = sxy + x[i] * y[i]
                  sx = sx + x[i]
                  sy = sy + y[i]
                  sxx = sxx + x[i] * x[i]
              k = (n * sxy - sx * sy) / (n * sxx - sx * sx) # incline_coeff
              b = (sy - k * sx) / n # shift_value
              return (k, b)
    else: raise ValueError("input array is more than two-dimensional")