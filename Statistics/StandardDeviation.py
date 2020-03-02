import numpy as np

#reference: https://docs.python.org/3/library/statistics.html

class StandardDeviation():
    @staticmethod
    def standard_deviance(data):
        return np.std(data)