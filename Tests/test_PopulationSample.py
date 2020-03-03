import unittest
from numpy.random import seed
from numpy.random import randint
from pprint import pprint

from PopulationSamples.CochransSample import Cochran
from PopulationSamples.ConfidenceIntervalPopulation import ConfidenceIntervalPopulation
from PopulationSamples.ConfidenceIntervalSample import ConfidenceIntervalSample
from PopulationSamples.KnownPopulation import KnownPopulation
from PopulationSamples.MarginError import MarginError
from PopulationSamples.RandomSample import RandomSample
from PopulationSamples.SystemicSample import SystemicSample
from PopulationSamples.UnknownPopulation import UnknownPopulation

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(3)
        self.testData = randint(0, 50, 15)
        #pprint(self.testData)

    def test_RandomSample(self):
        #creates a random sample for testing
        sample = RandomSample.random_sample(seed_=3, self.testData, lstLen=5)
        self.assertEqual(sample, [8, 41, 43, 3, 21])

    def test_SystematicSample(self):
        result = SystemicSample.systemicSample(self.testData)
        self.assertEqual(result, [3, 21, 43, 21, 20])

    def test_ConfidenceIntervalPopulation(self):
        result = ConfidenceIntervalPopulation.confidence_interval(confidence=.90, data=self.testData)
        self.assertEqual(result, (15.581632402905116, 28.68503426376155))

    def test_ConfidenceIntervalSample(self):
        result = ConfidenceIntervalSample.confidenceInterval(confidence=.90, data=self.testData, seed=3, high=)
        self.assertEqual(result, (5.6669372302865675, 40.73306276971343))

    def test_MarginError(self):
        result =MarginError.margin(data=self.testData, seed=3)
        #pprint(result)
        self.assertEqual(result, -14.133333333333335)

    def test_Cochran(self):
        result =Cochran.cochran(data=self.testData, lstLen=4, seed=3)
        self.assertEqual(result, 0.0010094984628091588)

    def test_UnkownPopulation(self):
        #generates a sample size of unknown population for testing
        result = UnknownPopulation.unknown_pop_sample(data=self.testData, seed=3, percent=0.41)
        self.assertEqual(result, 0.0012487381269214882)

    def test_KnownPopulation(self):
        #generates sample size of known population for testing
        result = KnownPopulation.known_pop_sample(data=self.testData, seed=3)
        self.assertEqual(result, 1.0)


if __name__ == '__main__':
    unittest.main()