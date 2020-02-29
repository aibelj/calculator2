from Statistics.Mean import Mean
from Statistics.Variance import Variance
from Statistics.StandardDeviation import StandardDeviation

#reference https://realpython.com/python-statistics/

class Skew():

    @staticmethod
    def skewness (data):

        dataLen = len(data)

        mn = Mean.mean(data)
        var = Variance.variance(data)
        std = StandardDeviation.standard_deviance(data)

        skew = (sum((item - mn)**3 for item in data)* dataLen / ((dataLen - 1) * (dataLen - 2) * std**3))

        return skew