import numpy as np

#source: https://realpython.com/python-statistics/

def quartiles(data, percentile):
    '''
    percentile() takes several arguments. You have to provide the dataset as
    the first argument and the percentile value as the second. The dataset can be in the
    form of a NumPy array, list, tuple, or similar data structure. The percentile
    can be a number between 0 and 100
    '''
    solution = np.percentile (data, percentile)
    return solution

