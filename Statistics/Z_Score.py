from Statistics.Mean import Mean
from Statistics.StandardDeviation import StandardDeviation
from Calculator.Division import division

Class ZScore():
    @staticmethod
    def z_score(a, b, c):

        a = int(a)
        b = int(b)
        c = int(c)
        value = [a,b,c]
        std_dev = StandardDeviation.standard_deviance(a, b, c)
        mn = Mean.mean(a, b, c, 3)
        result = division((a - mn ), std_dev)

        return result