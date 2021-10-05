import numpy as np

np.random.seed(42)
M = 100*np.random.rand(9,7).round(2)

# Task 1: Print the first and the last row with one slice operation

print(M[::len(M)-1,::])

# Task 2: Print all elements less than 10

print(M[M < 10]) # the M < 10 instruction returns one matrix of booleans with the condition applied to every element of the array 

# Task 3: Print each even row

print(M[::2,::])

# Task 4: Print each odd column

print(M[::,1::2])

# Task 5: Print the elements of the even rows and the odd columns

print(M[::2,1::2])

# Task 6: Print all elements from the following matrix with a pair of even indices

M1 = 100*np.random.rand(5,7).round(2)

print(M1[::2,::2])
