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
        seed(seed=5)
        self.testData = randint(low=0, high=50, size=15)
        self.testData2 = randint(low=1, high=51, size=15 )
        #pprint(self.testData)
        #pprint(self.testData2)

    def test_covariance(self):
        covariance = Covariance.covariance(data1=self.testData, data2=self.testData2)
        #pprint(covariance)
        self.assertEqual(covariance, -19.961904761904755)

    def test_mean(self):
        mean = Mean.mean(data=self.testData)
        self.assertEqual(mean, 25.466666666666665)

    def test_meanDeviation(self):
        meanDeviation = MeanDeviation.mean_deviation(data=self.testData)
        self.assertEqual(meanDeviation, 12.835555555555555)

    def test_median(self):
        median = Median.median(data=self.testData)
        self.assertEqual(median, 27.0)

    def test_mode(self):
        mode = Mode.mode(data=self.testData)
        self.assertEqual(mode, 16)

    def test_populationCorrelation(self):
        result = PopulationCorrelation.correlation(data1=self.testData, data2=self.testData2)
        self.assertEqual(result, -0.09958703367427517)

    def test_populationProportion(self):
        result = PopulationProportion.proportion(data=self.testData, lstLen=4, seed=3)
        self.assertEqual(result, 0.26666666666666666)

    def test_quartiles(self):
        quartiles = Quartiles.quartile(data=self.testData)
        self.assertEqual(quartiles, (13.0, 27.0, 37.0))

    def test_sampleCorrelation(self):
        result = SampleCorrelation.correlation(data1=self.testData, data2=self.testData2, seed=3)
        self.assertEqual(result, -0.5940762068478092)

    def test_skew(self):
        skewness = Skewness.skewness(data=self.testData)
        self.assertEqual(skewness, 0.15182604770872699)

    def test_standardDeviation(self):
        standardDeviation = StandardDeviation.standard_deviance(data=self.testData)
        self.assertEqual(standardDeviation, 14.01364414498321)

    def test_variance(self):
        variance = Variance.variance(data=self.testData)
        self.assertEqual(variance, 196.3822222222222)

    def test_z_score(self):
        z_score = Z_Score.zscore(data=self.testData, seed=2)
        self.assertEqual(z_score, -1.3177633508895406)


if __name__ == '__main__':
    unittest.main()


