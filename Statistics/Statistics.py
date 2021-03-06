'''
#from previous work assignment

from Calculator.Calculator import Calculator
from Statistics.Mean import Mean
from Statistics.Mode import Mode
from Statistics.Median import Median
from Statistics.StandardDeviation import StandardDeviation
from Statistics.Variance import Variance



class Statistics(Calculator):

    data = []

    def mean(self, data):
        self.result = Mean.mean(data)
        return self.result

    def mode(self, data):
        self.result = Mode.mode(data)
        return self.result

    def median (self, data):
        self.result = Median.median(data)
        return self.result

    def standard_deviance (self, data):
        self.result = StandardDeviation.standard_deviance(data)
        return self.result

    def variance (self, data):
        self.result = Variance.variance(data)
        return self.result

'''
