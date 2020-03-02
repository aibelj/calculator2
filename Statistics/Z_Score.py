from Statistics.Mean import Mean
from Statistics.StandardDeviation import StandardDeviation
from Calculator.Division import division



class Z_Score:
    @staticmethod
    def zscore(data):
        z = subtraction(data, Mean.mean(data))
        zscore = division(z, StandardDeviation.standard_deviance(data))
        return zscore