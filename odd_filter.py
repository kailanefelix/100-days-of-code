import numpy as np

## extract all odd numbers from an array:

a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

odd_filter = a % 2 != 0

print(a[odd_filter]) # it works!

## replace odd items

a[odd_filter] = 0 # it works!

print(a)

## replace odd items without affecting the original array 

# first way: copy the array and add the filter 
new_arr = a.copy()
new_arr[odd_filter] = 0
print(new_arr, a)


# second way: directly

new_a = np.where(a % 2 != 0, 0, a)
print(new_a, a)

# you can run the code without the 13th line to confirm that this way does not change the original values of a