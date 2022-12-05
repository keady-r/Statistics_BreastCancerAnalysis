#Functions to run across multiple Jupyter Notebooks. 
    #Shape - show the number of rows and columns in a data set 
def shape(data):
    print('='*20,'Dataset Shape','='*20)
    print(data.shape)
    print('\n')
    #Info - Show number of row/columns with row/column names and data type i.e if the data in the rows are int/float/oject etc. 
def info(data):
    print('='*20,'Dataset Info','='*20)
    print(data.info())
    print('\n')
    #Describe - Calculates, count, mean , std, min, max, 25%, 50%, 75% of each column
def describe(data):
    print('='*20,'Dataset Describe','='*20)
    print(data.describe())
    print('\n')

def getProbability(measure, total):
    probability = measure/total
    print("The Probability is:", round(probability,2))
