from scipy.stats import sem
from scipy.stats import t
from PopulationSamples.ConfidenceIntervalPopulation import ConfidenceIntervalPopulation
from PopulationSamples.RandomSample import RandomSample

class ConfidenceIntervalSample():
    @staticmethod
    def confidenceInterval(confidence, data, seed, high):
        data = RandomSample.random_sample(seed, data, high)
        cip = ConfidenceIntervalPopulation.confidence_interval(confidence, data)
        return cip