'''
#notes from tutoring session



#class RandomNumGen and its random methods

from random import random
import unittest
import numpy as np
from numpy.random import seed
from RandomNumGen.RandomNumber import random_ints
from numpy.random import randint
import pprint

class Random:

    below is an idea how I can individualize the functions:

    def random(self, low: float, high:float, seed = None):
        if seed is None:

    def random(self, low: int, high: int, seed=None):
        if seed == None:


    def randomInteger(self, low, high, seed=None):

    def random_num_noSeed(self, low, high, step):
        #Generates a random number without a seed between a range of two numbers - Integer
        random_int = random.randrange(low, high, step)
        return random_int

    def random_flt_noSeed (self, low, high, decimalPlace):
        # Generates a random number without a seed between a range of two numbers - Decimal rounded to the specified decimal place
        random_flt = round(random.uniform(low, high), decimalPlace)
        return random_flt


    def random_int_seed(self, low, high, seed_):
        #Generate a random integer with a seed between a range of two numbers (low, high)
        random.seed (seed_)
        random_int = random.randint(low, high, 1)
        return random_int

    def random_flt_seed(self, low, high, seed_):
        # Generate a random float with a seed between a range of two numbers - (low, high)
        random.seed (seed_)
        random_flt =  round(random.uniform(low, high), 2)
        return random_flt

    def random_ints_seed(self, numRange, lstLen, seed_):
        #np.arrange(listLen).reshape(1,1, listLen)
        # Generates a list of N random numbers with a seed and between a range of numbers - Integer
        #source: https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.random.random_sample.html

        random.seed(seed_)
        random_ints = random.sample(range(numRange), lstLen)
        return random_ints

    def random_flts_seed(self, numRange, lstLen, seed_):
        # Generates a list of N random numbers with a seed and between a range of numbers - Decimal
        #source: https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.random.random_sample.html

        np.random.seed(seed_)
        random_flts = np.random.random_sample((lstLen,))
        return random_flts

    def random_item_lst (self, lst):
        # user passes a list and a random item is selected

        selection = random.choice(lst)
        return selection

    def random_num (self, numRange, lstLen):
        #a random list of integers is generated and a random num is selected and returned
        #source: https://realpython.com/python-random/
        nums = random_ints(numRange, lstLen)
        num = random.choice(nums)
        return num


    def n_num_items_frmLst(self, numRange, lstLen, size):
        #6. Select N number of items from a list without a seed
        #source: https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.choice.html

        #generates a random sample
        nums = random_ints(numRange, lstLen)

        n = size

        newLst = np.random.choice(nums, n, replace=False, p=None)
        return newLst

    def n_num_items_seedLst(self, numRange, listLen, seed_, size):
        #7.  Select N number of items from a list with a seed
        #Source: https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.choice.html

        lst = self.random_ints_seed(numRange, lstLen, seed_)

        newLst = np.random.choice(lst, size, replace=False, p=None)

        return newLst

'''

