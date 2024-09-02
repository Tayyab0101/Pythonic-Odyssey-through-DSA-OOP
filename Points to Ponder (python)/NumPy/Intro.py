import numpy as np

list1 = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], ["A", "B", "C"]]]
array1 = np.array(list1)
# print(array1)
print(type(array1)) 
print(f"Its a {np.ndim(array1)} dimensional array") # Number of dimensions
print("Shape of the array:", np.shape(array1)) 
print("Number of elements in the array:", np.size(array1))  # Number of elements
print("Size of a single array element in bytes:", array1.itemsize)
print("Data type of array is", array1.dtype) # int32, float64, U6 for string, U11 for mix
print(array1[0, 1:]) # Slicing or like aray1[0][1][2]

array3 = np.arange(1, 7).reshape((2, 3)) # print a range from 1-6, reshape(rows, columns)
print(array3)

array4 = np.zeros(5, dtype=int) # without type it will print float
print(array4)



