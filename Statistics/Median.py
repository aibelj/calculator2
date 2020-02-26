from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Division import division


def median (data):
    dataLen = len(data)

    data = data.sort()

    if dataLen % 2 == 0:
        medianHi = data[dataLen//2]
        medianLow = data[subtraction((dataLen//2),1)]
        median = division(addition(medianHi,medianLow), 2)
    else:
        median = data[dataLen//2]

    return median