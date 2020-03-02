from Statistics.StandardDeviation import StandardDeviation
from Statistics.Z_Score import Z_Score


class MarginError():
    @staticmethod
    def margin(data,seed):
        z_score = Z_Score.zscore(data, seed)
        stdDev = StandardDeviation.standardDeviation(data)
        return z_score * stdDev
