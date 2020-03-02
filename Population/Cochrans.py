from Statistics.Z_Score import Z_Score
from PopulationSamplingFunctions.marginOfError import MarginOfError
from StatisticsFunctions.populationProportion import PopulationProportion
from Calculator.Exponentiation import exponentiation


class Cochran():
    @staticmethod
    def cochran(theSeed, data, rangeNumber):
        # z = z-score
        # p = proportion population
        # e = margin of error

        z = Z_score.z_score(theSeed, data)
        p = PopulationProportion.proportion(theSeed, data, rangeNumber)
        e = MarginOfError.margin(theSeed, data)
        q = 1 - p

        cochran = (exponentiation(z,2) * p * q)/exponentiation(e,2)

        return cochran