import random
from RandomNumGen.RandomNumber import RandomNumber

class RandomList:

    @staticmethod
    def random_list(low, high, length, seed):
        #creates a list of random numbers by callin random_number_seed method
        data = []

        while True:
            number = RandomNumber.random_number_seed(low, high, seed)
            data.append(number)

            if len(data) == length:
                break

        return data