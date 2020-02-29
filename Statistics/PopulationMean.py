from Calculator.Addition import addition
from Calculator.Division import division



def population_mean(data):
    dataLen = len(data)
    total = 0
    for item in data:
        total = addition(total, item)
    return division(total, dataLen)