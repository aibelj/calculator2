from Calculator.Square import squaring
from Statistics.Z_Score import Z_Score
from Statistics.StandardDeviation import StandardDeviation
from PopulationSamples.MarginError import MarginError

class KnownPopulation():
    @staticmethod
    def sampleSize(data, seed):

        z_s = Z_Score.zscore(data, seed)
        m_e = MarginError.margin(data, seed)
        s_d = StandardDeviation.standard_deviance(data)

        value = (z_s * s_d) / m_e

        popSample = squaring(value)

        return popSample