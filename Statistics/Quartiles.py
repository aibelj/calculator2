import numpy as np

#source: https://realpython.com/python-statistics/

class Quartiles:
    '''
    percentile() takes several arguments. You have to provide the dataset as
    the first argument and the percentile value as the second. The dataset can be in the
    form of a NumPy array, list, tuple, or similar data structure. The percentile
    can be a number between 0 and 100
    '''

    @staticmethod
    def quartile1(data):
        solution = np.percentile(data,[25])
        return solution

    @staticmethod
    def quartile2(data):
        solution = np.percentile(data, [50])
        return solution

    @staticmethod
    def quartile3(data):
        solution = np.percentile(data, [75])
        return solution


