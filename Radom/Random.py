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

    def random_item_lst (self, lst):
        # Select a random item from a list

        lst_len = len(lst)

        random_int_flt = self.random_num_noSeed(0, lst_len)
        '''ask prof why pass to self when calling random_num_noSeed??'''

        random_int = random_int_flt[0]

        return lst[random_int]

    def random_num_fromList (self, numRange, lstLen):
        '''question 5: Set a seed and randomly.select the same value from a list - further clarify'''

        num_lst = self.random_lst_seed(numRange, lstLen)

        #random.choice selects a random item from a list

        random_num = random.choice(num_lst)

        return random_num

    def n_num_items_frmLst(self, lst, size):
        #6. Select N number of items from a list without a seed
        #source: https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.choice.html
        ''' do you want uniqure numbers every time or can it have duplicates '''

        #this returns a list/array
        newLst = np.random.choice(lst, size, replace=False, p=None)

        return newLst

    def n_num_items_seedLst(self, numRange, listLen, size):
        #7.  Select N number of items from a list with a seed

        lst = self.random_lst_seed(numRange, lstLen)

        newLst = np.random.choice(lst, size, replace=False, p=None)

        return newLst