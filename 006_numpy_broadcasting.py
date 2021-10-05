# Broadcasting is simply a set of rules for applying binary ufuncs on arrays of different sizes.

# Rule 1: If the two arrays differ in their number of dimensions, the shape of the one with fewer dimensions is padded with ones on its leading (left) side

# Rule 2: If the shape of the two arrays does not match in any dimension, the array with shape equal to 1 in that dimension is stretched to match the other shape

# Rule 3: If in any dimension the sizes disagree and neither is equal to 1, an error is raised

# it's like magic: There's no extra memory being actually allocated in the course of this operation!

# Examples:

import numpy as np

a = np.arange(3)
print(a+5)

b = np.ones((3,3))
c = np.arange(3)
print(b+c)

d = np.arange(3).reshape(3,1)
print(d+c)