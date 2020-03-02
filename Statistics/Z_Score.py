from Statistics.StandardDeviation import StandardDeviation
from Statistics.Mean import Mean
from RandomNumGen.ItemReturnType import ItemReturnType

class Z_Score:
    @staticmethod
    def zscore(data, seed):
        n = ItemReturnType.random_num_seed(data, seed)
        mn = Mean.mean(data)
        sd = StandardDeviation.standard_deviance(data)
        zs = (n - mn) / sd
        return zs