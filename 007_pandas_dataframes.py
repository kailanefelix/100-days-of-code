import pandas as pd

gp = pd.read_csv('gapminder.tsv.txt', sep='\t') # open the csv file and separete in tabs

type(gp) # returns the type of "gp" (we have a dataframe!!!)

gp.shape # returns (rows, columns), shape is an atribute

gp.info() # info is a method // a single column has to be the same type and object is probabily a string

gp.head() # returns the first five rows of the dataset

gp.tail() # returns the last five rows of the dataset

gp.columns # returns the title of the columns

gp.index # returns the create command of these indexes, so it's not going to be storing

gp.values[0] # returns the first row of values

gp.dtypes # returns the data type of each column

# subset and dataframe:

country = gp['country'] # returns "pandas.core.series.Series"

type(country) # one pandas series is just an extension of a numpy array

country = gp[['country']] # returns the subset as a dataframe

gp.drop('continent', axis=1) # returns the dataframe without the column "continent"

# functions loc and iloc:

# loc = index label, this function do something like a string match with the index of dataframe, it's not an indexing
gp.loc[-1] # error!
gp.loc[[0]] # returns the first row as a dataframe
gp.loc[[0, 1]] # returns the first two rows as a dataframe

# iloc = actually the index (accept negative numbers!)
gp.iloc[[0, 1, -2]]

# subset rows and columns:

subset = gp.loc[:,['year', 'pop']]

subset = gp.iloc[:,[2, 4]]
subset.head()

# subset with boolean conditions:

gp.loc[gp['country'] == 'United States'] # returns all the values witch country is "United States"
gp.loc[gp['country'] == 'United States', ['country', 'year', 'lifeExp']]