import random
from RandomNumGen.RandomNumber import RandomNumber
from RandomNumGen.RandomList import RandomList

class ItemReturnType:

    @staticmethod
    def random_num(data):
        #returns random number from a list (NO seed)
        num = random.choice(data)
        return num

    @staticmethod
    def random_num_seed(data, seed):
        # returns random number from a list (WITH seed)
        random.seed(seed)
        num = ItemReturnType.random_num(data)
        return num

    @staticmethod
    def aList(data, lstLen):
        lst = []
        while True:
            num = ItemReturnType.random_num(data)
            lst.append(num)
            if len(lst) < lstLen:
                continue

        return lst

    @staticmethod
    def aList_seed(data, lstLen, seed):
        random.seed(seed)
        lst = ItemReturnType.aList(data, lstLen)
        return lst
