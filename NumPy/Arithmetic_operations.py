# Arrays are best method for storing mathematical Data

import numpy as np 

x = np.array([[1, 2], [3, 4]])
y = np.array([[11, 12], [13, 14]])
# Size must be equal for any kind of operation
print(x + y) 
print(y - x)
print(x * y)
print(x @ y) #matrix multiplication
print(y / x)
print( y // x)
print(y ** x)
print(y % x)
print(x.transpose())
