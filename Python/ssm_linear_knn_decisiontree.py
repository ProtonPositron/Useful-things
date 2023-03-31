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
    
def entropy(class_y):
    """
    Calculate a value of entropy of list of class labels

    INPUT:

        - class_y: list of class labels

    OUTPUT:

        - the entropy value
    """
    if len(class_y) <=1: #Trivial case
        return 0
    
    total_count = np.bincount(class_y) #Count number of each labels
    probabilities = total_count[np.nonzero(total_count)]/len(class_y) #Find the probabilities of each label in all list
    if len(probabilities) <= 1: #Trivial case
        return 0 
    return - np.sum(probabilities*np.log(probabilities))/np.log(len(probabilities))# This is an entropy for any number of classes and normalized to 1 - maximum

def information_gain(initial_y, splitted_y):
    """
    Calculation of information gain after splitting on parts.
    
    INPUT:
    
      - initial_y: original distribution of labels
      - splitted_y: distribution after splittining, consist of several elements (basic - two) that together is equal to initial_y
      
    INPUT EXAMPLE:
      - initial_y: [0,0,0,1,1,1]
      - splitted_y: [[0,0],[0,1,1,1]]
      
    OUTPUT:
    
      - info_gain: the information gain
    """
    conditional_entropy = 0
    for y in splitted_y:
        conditional_entropy += (entropy(y)*len(y)/len(initial_y))
    info_gain = entropy(initial_y) - conditional_entropy
    return info_gain

def partition_classes(x, y, split_attribute, split_val):
    """
    Partition on two sides by split_value in split_attribute
    
    INPUT:
    
      -x                : initial Data
      -y                : a list of labels
      -split_attribute  : column for splitting
      -split_val        : value for splitting (num or cat)
      
    OUTPUT:
    
      - x_left            : left part of x
      - x_right           : right part of x
      - y_left            : left part of y
      - y_right           : right part of y
    """

    x = np.array(x)
    column_split = x[:, split_attribute]
    x_left = []
    y_right = []
    x_right = []
    y_left = []

    counter = 0

    if isinstance(split_val, str) == False: # Numerical?
        for i in column_split:
            if i <= split_val:
                x_left.append(x[counter])
                y_left.append(y[counter])
            else:
                x_right.append(x[counter])
                y_right.append(y[counter])
            counter +=1
    else: # Categorical
        for i in column_split:
            if i == split_val:
                x_left.append(x[counter])
                y_left.append(y[counter])
            else:
                x_right.append(x[counter])
                y_right.append(y[counter])
            counter +=1
    return x_left, x_right, y_left, y_right

def find_best_split(x, y, split_attribute):
    """
    Calculate best split value and info gain for entered split attribute
    
    INPUT:
    
      -x: initial Data
      -y: a list of labels
      -split_attribute: column of split
      
    OUTPUT:
    
      -best_split_val: optimal split value
      -best_info_gain: optimal split gain info
    """
    best_info_gain = 0
    x = np.array(x)
    column_split = x[:,split_attribute]
    column_split = np.unique(column_split)
    best_split_val = column_split[0]

    for split_val in column_split:
        current_x_left, current_x_right, current_y_left, current_y_right = partition_classes(x, y,split_attribute, split_val)
        current_y = []
        current_y.append(current_y_left)
        current_y.append(current_y_right)
        current_info_gain = information_gain(y, current_y)
        if current_info_gain > best_info_gain:
            best_info_gain = current_info_gain
            best_split_val = split_val
    return best_split_val, best_info_gain

def find_best_feature(x, y):
    """
    Define an optimal feature and value for splitting to maximize info gain

    INPUT:

        - x: initial Data
        - y: a list of classes

    OUTPUT:

        - best_feature: optimal feature for splittting (maximum info gain)
        - best_split_val: optimal value of splitting to maximize info gain
    """
    best_info_gain = 0
    best_feature = 0
    best_split_val = 0
    for feature_index in range(len(x[0])):
        current_best_split_val, current_best_info_gain = find_best_split(x, y, feature_index)
        if current_best_info_gain > best_info_gain:
            best_info_gain = current_best_info_gain
            best_feature = feature_index
            best_split_val = current_best_split_val
    return best_feature, best_split_val

class MyDecisionTree(object):
    def __init__(self, max_depth = None):
        """
        INPUT:
        
            - max_depth: max depth of the tree including the root node.
        """
        self.tree = {}
        self.residual_tree = {} #For predictrion
        self.max_depth = max_depth
    
    def fit(self, x, y, depth):
        """
        Create a dictionary with data, labels and deapth
        """
        unique_labels = np.unique(y)
        if (len(unique_labels) == 1) or (depth == self.max_depth): # This is a Leaf, the end of branch
            unique_labels, counts_unique_labels = np.unique(y, return_counts = True)
            index = counts_unique_labels.argmax()
            classification = unique_labels[index]
            return classification

        best_feat, best_split = find_best_feature(x, y)        
        x_left, x_right, y_left, y_right = partition_classes(x, y, best_feat, best_split)

        if isinstance(best_split, str):
            question = "{} == {}".format(best_feat, best_split)
        else:
            question = "{} <= {}".format(best_feat, best_split)
        node = {question: []}

        depth +=1
        yes_answer = self.fit(x_left, y_left, depth) # Recurrent part that creates a branches
        no_answer = self.fit(x_right, y_right, depth)

        if yes_answer == no_answer:
            node = yes_answer
        else:
            node[question].append(yes_answer)
            node[question].append(no_answer)
        self.tree = node
        return node

    def predict(self, record, flag = 1):
        """
        Classify a sample in test data set using self.tree and return the predictes label
        
        INPUT:

            - record: a single data point that should be classidied
    
        OUTPUT:
        
            - answer: a class that a model predict for this point

        classify a sample in test data set using self.tree and return the predictes label
        """
        if flag == 1:
            self.residual_tree = self.tree
        question = list(self.residual_tree.keys())[0]
        feature, comparison, value = question.split()

        if comparison == "==": # String
            if record[int(feature)] == value:
                answer = self.residual_tree[question][0]
            else:
                answer = self.residual_tree[question][1]
        elif comparison == "<=": # Integer
            if record[int(feature)] <= float(value):
                answer = self.residual_tree[question][0]# Right
            else:
                answer = self.residual_tree[question][1]# Left

        if not isinstance(answer, dict): # Base case, find the answer
            return answer
        else: # Recursion
            self.residual_tree = answer
            return self.predict(record, 0)
