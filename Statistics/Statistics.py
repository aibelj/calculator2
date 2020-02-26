from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Mode import mode
from Statistics.Median import median
from Statistics.StandardDeviation import standard_deviance
from Statistics.Variance import variance
from Statistics.Quartiles import quartiles


class Statistics(Calculator):

    data = []

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def median (self, data):
        self.result = median(data)
        return self.result

    def standard_deviance (self, data):
        self. result = standard_deviance(self, data)
        return self.result

    def variance (self, data):
        self.result = variance(self, data)
        return self.result

    def quartiles (self, data, percentile):
        self.results = quartiles(data, percentile)
        return self.results
