import random from random


def random_ints(self, numRange, lstLen):
    #generates a list of random integers

    random_ints = random.sample(range(numRange), lstLen)
    return random_ints