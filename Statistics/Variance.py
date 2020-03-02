import numpy as np

class Variance():
    @staticmethod
    def variance(data):
        return np.var(data)




'''
#alternative:
import statistics

#reference: https://docs.python.org/3/library/statistics.html
class Variance():
    @staticmethod
    def variance (data):
        solution = statistics.variance(data, xbar=None)

        return solution
'''