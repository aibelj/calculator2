#Random class
#random methods

from random import random
import unittest
import numpy as np
from numpy.random import seed
from numpy.random import randint
import pprint

class Random:

    def random_num_noSeed(self, low, high):
        #Generates a random number without a seed between a range of two numbers - Integer
        random_int = random.randrange(low, high, 1)

        # Generates a random number without a seed between a range of two numbers - Decimal rounded to the hundredth place
        random_flt = round(random.uniform(low, high),2)

        return (random_int, random_flt)

    def random_num_seed(self, low, high):
        #Generate a random number with a seed between a range of two numbers - Integer
        random.seed (5)
        random_int = random.randint(low, high, 1)

        # Generate a random number with a seed between a range of two numbers - Decimal
        random.seed (5)
        random_flt =  round(random.uniform(low, high), 2)

        return (random_flt, random_int)

    def random_lst_seed(self, numRange, lstLen):

        #np.arrange(listLen).reshape(1,1, listLen)
        # Generates a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal
        #integer

        random.seed(5)
        random_ints = random.sample(range(numRange), lstLen)


        # Decimal
        #source: https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.random.random_sample.html
        np.random.seed(5)
        random_flts = np.random.random_sample((lstLen,))

        return (random_flts, random_ints)




