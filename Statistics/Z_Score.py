from Statistics.Mean import mean
from Statistics.StandardDeviation import standard_deviance
from Calculator.Division import division

def z_score(a, b, c):

    a = int(a)
    b = int(b)
    c = int(c)
    value = [a,b,c]
    std_dev = standard_deviance(a, b, c)
    mn = mean(a, b, c, 3)
    result = division((a - mn ), std_dev)

    return result