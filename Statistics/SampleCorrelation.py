from Calculator.Multiplication import multiplication
from Statistics.Covariance import Covariance
from Statistics.StandardDeviation import StandardDeviation
from RandomNumGen.ItemReturnType import ItemReturnType

class SampleCorrelation():
    @staticmethod
    def correlation(data1, data2, seed):
        # population sample with seed
        pop1 = ItemReturnType.aList_seed(data1, 5, seed)
        pop2 = ItemReturnType.aList_seed(data2, 5, seed)

        cv = Covariance.covariance(pop1, pop2)

        stdDev1 = StandardDeviation.standard_deviance(pop1)
        stdDev2 = StandardDeviation.standard_deviance(pop2)

        sc = cv/(multiplication(stdDev1,stdDev2))

        return sc
