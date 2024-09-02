import numpy as np 

x = np.array([[1, 34, 23], [45, 12, 25], [76, 23, 34]])
y = np.sort(x)
z = np.sort(x, axis=0) # for column wise sorting
yz = np.argsort(x) # to sort and print only index; axis = 1 means row-wise
print(y)
print(z)
print(yz)

x.sort() # to make changes in same memory position row-wise or column wise
print(x)

a = [2, 5, 8, 3, 4, 1]
b = np.sort(a)[::-1] # sort in reverse orderr
print(b)
# Statistical Oprayions
print("Max:", b.max())   # for list we do like max(a) and for array a.max() / np.mean(a)
print("Min:", b.min())
print("Sum:", b.sum())
print("Mean:", np.mean(b))
print("Median:", np.median(b))
print("Product:", b.prod())
print("Variance:", b.var())
print("Standard Deviation:", b.std())