from Statistics.Z_Score import Z_Score
from Population.MarginError import MarginError
from StatisticsFunctions.populationProportion import PopulationProportion
from Calculator.Exponentiation import exponentiation


class Cochran():
    @staticmethod
    def cochran(data, seed, rangeNumber):
        # z = z-score
        # p = proportion population
        # e = margin of error

        z = Z_score.z_score(theSeed, data)
        p = PopulationProportion.proportion(theSeed, data, rangeNumber)
        e = MarginError.margin(data,seed)
        q = 1 - p

        cochran = (exponentiation(z,2) * p * q)/exponentiation(e,2)

        return cochran