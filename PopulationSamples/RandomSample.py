from RandomNumGen.ItemReturnType import ItemReturnType
from numpy.random import seed

class RandomSample():
    @staticmethod
    def random_sample(seed_, data, lstLen):
        seed(seed_)
        return ItemReturnType.aList_seed(data, lstLen)