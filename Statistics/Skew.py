from Statistics.Mean import Mean
from Statistics.Variance import Variance
from Statistics.StandardDeviation import standard_deviance

#reference https://realpython.com/python-statistics/

class Skew():

    @staticmethod
    def skewness (data):

        dataLen = len(data)

        mn = mean(data)
        var = variance(data)
        std = standard_deviance(data)

        skew = (sum((item - mn)**3 for item in data)* dataLen / ((dataLen - 1) * (dataLen - 2) * std**3))

        return skew


    
