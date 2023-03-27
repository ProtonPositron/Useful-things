"""
    Some useful functions for Linear Regression, K Nearest Neighbours and Decision Tree methods
"""
# Author: Sergei Starkov

import numpy as np

def SSMLinearRegression (x: type = np.ndarray, y: type = [np.ndarray, None]):
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
    if isinstance (x, np.ndarray): #Check if it is ndarray
            if x.ndim <= 2: #Check array dimensional
                    if x.ndim == 2:
                        if x.shape[0] > 2 and x.shape[1] > 2:
                            raise ValueError("Number of rows or columns is more than two")
                        elif x.shape[0] == 2: # Modify two-dimension array in two one-dimension arrays
                            y = x[1,:]
                            x = x[0,:]
                        elif x.shape[1] == 2:
                            y = x[:,1]
                            x = x[:,0]
                    n = len(x)
                    _ = 0 # Error flag
                    try:
                            if y == None: _ = 1 # Try if y is "None"
                    except AttributeError:
                            if len(y) != n: # Check if x and y have a different size (it is known that y is not "None")
                                    raise ValueError ("The numbers of values in two rows are different")
                                    _ = 1 # If x and y have different size than error flag is active
                            else: _ = 0 # x and y is ok and ready to calculate, error flag is not active
                    else:       
                            _ = 1 # y is "None" and not modified from second row of x so error flag is active
                            raise ValueError ("There is only one row or type of Data is not numpy.ndarray")
                    finally:
                            if not _: # Calculate if error flag is not active
                                    sxy = 0 # Define temporary parameters
                                    sx = 0
                                    sy = 0
                                    sxx = 0
                                    for i in range(0, n): # Construct one cycle for minimum processing
                                        sxy += x[i] * y[i]
                                        sx += x[i]
                                        sy += y[i]
                                        sxx += x[i] * x[i]
                                    k = (n * sxy - sx * sy) / (n * sxx - sx * sx) # incline_coeff
                                    b = (sy - k * sx) / n # shift_value
                                    return (k, b)
            else: raise ValueError("Input array is more than two-dimensional")
    else: raise ValueError("Type of Data is not numpy.ndarray")
