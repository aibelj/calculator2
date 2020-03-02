from Calculator.Square import squaring
from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Statistics.Z_Score import Z_Score
from PopulationSamples.MarginError import MarginError

class UnknownPopulation():
    @staticmethod
    def unknown_pop_sample(data, seed, percent):

        z_s = Z_Score.zscore(data, seed)
        m_e = MarginError.margin(data, seed)
        p = percent
        q = subtraction(1, p)

        val = division(z_s, m_e)
        samplePop = squaring(val) * p * q

        return samplePop