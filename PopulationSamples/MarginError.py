from Statistics.StandardDeviation import StandardDeviation
from Statistics.Z_Score import Z_Score
from Calculator.Multiplication import multiplication


class MarginError():
    @staticmethod
    def margin(data,seed):
        zs= Z_Score.zscore(data, seed)
        sd = StandardDeviation.standard_deviance(data)
        margin = multiplication(zs, sd)
        return margin
