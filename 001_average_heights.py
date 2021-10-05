# import the necessary libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn

seaborn.set() 

data = pd.read_csv('Documents\python\president_heights.csv') # read the csv data
heights = np.array(data['height(cm)']) # take just the height column

print("Median: ", np.median(heights))

print("Mean height: ", heights.mean()) 

print("Standard deviation:", heights.std()) ## compute standard deviation

print("Minimum height: ", heights.min()) ## find the minimum value

print("Maximum height: ", heights.max()) ## find the maximum value

# plot the histogram (frequency distribution) using matplotlib

plt.hist(heights) 
plt.title('Height of US Presidents')
plt.xlabel('height (cm)')
plt.ylabel('n° of presidents');

# now with the heights in meter:

heights_meter = heights * 10 ** - 2

plt.hist(heights_meter) 
plt.title('Height of US Presidents')
plt.xlabel('height (m)')
plt.ylabel('n° of presidents');
