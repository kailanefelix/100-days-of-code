import numpy as np

# np.sort returns a sorted version of the array without modifying the input 

x = np.array([2, 1, 4, 3, 5])
print(np.sort(x))


# argsort() returns the indices of the sorted elements 

x = np.array([2, 1, 4, 3, 5])
indices_x = np.argsort(x)
print(indices_x)

# these indices can then be used (via fancy indexing) to construct the sorted array:

print(x[indices_x])


# sorting along rows or columns (using the axis argument)

m = np.random.rand(10,2)
print(np.sort(m, axis=0)) # sort each column of m
print(np.sort(m, axis=1)) # sort each row of m

# partial sorts

# np.partition returns a new array with the smallest K values to the left of the partition, and the ramaining values on the right (without any order)

y = np.array([7, 9, 4, 5, 6, 2, 1, 4, 0])
print(np.partition(y, 4))
