This directory contains python modules.
Some functions may be unique, but some of them just my vision of known ones.
File: "testing_and_compare_moduls.py" contains testing programs which i use to compare perfomance and may be something else.

Results public here:

SSMLinearRegression vs sklearn.linear_model LinearRegression
Time of calculation in seconds

Test 1: 100 elements of x and y
Results of SSMLinearRegression
Incline_coeff is: [3.00313148]
Shift_value is:   [4.47933207]
Time of calculation 0.001950979232788086
Results of sklearn LinearRegression
Coef_: [[3.00313148]] 
Intercept_: [4.47933207]
Time of calculation 0.001950979232788086
Time of SSM/ time of sklearn: 1.0

Test 2: 1000 elements of x and y
Results of SSMLinearRegression
Incline_coeff is: [2.99577326]
Shift_value is:   [4.49474979]
Time of calculation 0.014631509780883789
Results of sklearn LinearRegression
Coef_: [[2.99577326]] 
Intercept_: [4.49474979]
Time of calculation 0.0009758472442626953
Time of SSM/ time of sklearn: 14.993647691180064

Test 3: 10 000 elements of x and y
Results of SSMLinearRegression
Incline_coeff is: [3.00322543]
Shift_value is:   [4.49416767]
Time of calculation 0.15218019485473633
Results of sklearn LinearRegression
Coef_: [[3.00322543]] 
Intercept_: [4.49416767]
Time of calculation 0.0019512176513671875
Time of SSM/ time of sklearn: 77.99242424242425

Test 4: 100 000 elements of x and y
Results of SSMLinearRegression
Incline_coeff is: [2.99970162]
Shift_value is:   [4.4998064]
Time of calculation 1.5257329940795898
Results of sklearn LinearRegression
Coef_: [[2.99970162]] 
Intercept_: [4.4998064]
Time of calculation 0.006829261779785156
Time of SSM/ time of sklearn: 223.41111576595446

Test 5: 1 000 000 elements of x and y
Results of SSMLinearRegression
Incline_coeff is: [3.00001596]
Shift_value is:   [4.4997782]
Time of calculation 14.897346019744873
Results of sklearn LinearRegression
Coef_: [[3.00001596]] 
Intercept_: [4.4997782]
Time of calculation 0.07316231727600098
Time of SSM/ time of sklearn: 203.62047806038487

Test 6: 10 000 000 elements of x and y
Results of SSMLinearRegression
Incline_coeff is: [3.00010051]
Shift_value is:   [4.49981545]
Time of calculation 148.69175052642822
Results of sklearn LinearRegression
Coef_: [[3.00010051]] 
Intercept_: [4.49981545]
Time of calculation 0.6994533538818359
Time of SSM/ time of sklearn: 212.5827972676329