from Statistics.Covariance import Covariance
from Statistics.StandardDeviation import StandardDeviation

class PopulationCorrelation():
    @staticmethod
    def correlation(data1, data2):
        cov = Covariance.covariance(data1, data2)
        stdDev1 = StandardDeviation.standard_deviance(data1)
        stdDev2 = StandardDeviation.standard_deviance(data2)
        cor = cov/(stdDev1*stdDev2)
        return cor

