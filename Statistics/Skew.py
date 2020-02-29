from Statistics.Mean import Mean
from Statistics.Median import Median
from Statistics.Mode import Mode
from Statistics.StandardDeviation import StandardDeviation
from Calculator.Division import division
from Calculator.Subtraction import subtraction



class Skew:

    @staticmethod
    def modeskew(data):
        n1 = subtraction(Mean.mean(data), Mode.mode(data))
        n2 = division(n1, StandardDeviation.standard_deviance(data))
        return n2

    @staticmethod
    def medianskew(data):
        n1 = subtraction(Mean.mean(data), Median.median(data))
        n2 = division(ni, StandardDeviation.standard_deviance(data))
        return n2