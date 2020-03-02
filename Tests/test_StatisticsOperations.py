import unittest
from numpy.random import seed
from numpy.random import randint
from pprint import pprint

from Statistics.Mean import Mean
from Statistics.Median import Median
from Statistics.MeanDeviation import MeanDeviation
from Statistics.Mode import Mode
from Statistics.PopulationCorrelation import PopulationCorrelation
from Statistics.Quartiles import Quartiles
from Statistics.SampleCorrelation import SampleCorrelation
from Statistics.Skew import Skewness
from Statistics.StandardDeviation import StandardDeviation
from Statistics.Variance import Variance
from Statistics.Z_Score import Z_Score
from Statistics.Covariance import Covariance
from Statistics.PopulationCorrelation import PopulationCorrelation
from Statistics.SampleCorrelation import SampleCorrelation
from Statistics.PopulationProportion import PopulationProportion


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(5)
        self.testData = randint(0, 50, 15)
        self.testData2 = randint(1, 51, 15 )
        #pprint(self.testData)
        #pprint(self.testData2)

    def test_covariance(self):
        covariance = Covariance.covariance(self.testData, self.testData2)
        #pprint(covariance)
        self.assertEqual(covariance, -19.961904761904755)

    def test_mean(self):
        mean = Mean.mean(self.testData)
        self.assertEqual(mean, 25.466666666666665)

    def test_meanDeviation(self):
        meanDeviation = MeanDeviation.mean_deviation(self.testData)
        self.assertEqual(meanDeviation, 12.835555555555555)

    def test_median(self):
        median = Median.median(self.testData)
        self.assertEqual(median, 27.0)

    def test_mode(self):
        mode = Mode.mode(self.testData)
        self.assertEqual(mode, 16)

    def test_populationCorrelation(self):
        result = PopulationCorrelation.correlation(self.testData, self.testData2)
        self.assertEqual(result, -0.09958703367427517)

    def test_populationProportion(self):
        result = PopulationProportion.proportion(self.testData, 4, 3)
        self.assertEqual(result, 0.26666666666666666)

    def test_quartiles(self):
        quartiles = Quartiles.quartile(self.testData)
        self.assertEqual(quartiles, (13.0, 27.0, 37.0))

    def test_sampleCorrelation(self):
        result = SampleCorrelation.correlation(self.testData, self.testData2, 3)
        self.assertEqual(result, -0.5940762068478092)

    def test_skew(self):
        skewness = Skewness.skewness(self.testData)
        self.assertEqual(skewness, 0.15182604770872699)

    def test_standardDeviation(self):
        standardDeviation = StandardDeviation.standard_deviance(self.testData)
        self.assertEqual(standardDeviation, 14.01364414498321)

    def test_variance(self):
        variance = Variance.variance(self.testData)
        self.assertEqual(variance, 196.3822222222222)

    def test_z_score(self):
        z_score = Z_Score.zscore(self.testData, 2)
        self.assertEqual(z_score, -1.3177633508895406)


if __name__ == '__main__':
    unittest.main()


