from Calculator.Division import division
from Calculator.Subtraction import subtraction
from RandomNumGen.RandomNumber import RandomNumber

class SystemicSample():
    @staticmethod
    def systemicSample(aLst):
        lenLst = len(aLst)
        num = (RandomNumber.random_number_seed(2, lenLst, seed=lenLst))
        nNum = round(division(num, 4))

        if nNum == 1:
            n =3

        sample = []
        temp = subtraction(nNum, 1)

        while temp <= subtraction(lenLst, 1):
            val = aLst[temp]
            sample.append(val)
            temp += nNum

        return sample