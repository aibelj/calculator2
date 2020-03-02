import numpy as np

#source: https://realpython.com/python-statistics/

class Quartiles():
    '''
    percentile() takes several arguments. You have to provide the dataset as
    the first argument and the percentile value as the second. The dataset can be in the
    form of a NumPy array, list, tuple, or similar data structure. The percentile
    can be a number between 0 and 100
    '''


    @staticmethod
    def quartile(data):
        quartile1 = np.quantile(data, .25)
        quartile2 = np.quantile(data, .50)
        quartile3 = np.quantile(data, .75)
        return quartile1, quartile2, quartile3

