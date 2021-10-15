# Do a function to generate a random float matrix and another to return the statistics of the values of the matrix:
# mean, median, standard deviation, min, and max.

import numpy as np
import pandas as pd

np.random.seed(0)
def matrix_generator(n,m):
  return np.random.rand(n,m)

def stats(m):

    mean = np.mean(m, axis = 0)
    median = np.median(m, axis = 0)
    std = np.std(m, axis = 0)
    min_value = np.min(m, axis = 0)
    max_value = np.max(m, axis = 0)

    rows = ['mean', 'median', 'std', 'min_value', 'max_value']
    stats = pd.DataFrame([mean, median, std, min_value, max_value], index = rows)

    return stats