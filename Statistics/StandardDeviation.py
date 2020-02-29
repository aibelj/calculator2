import statistics

#reference: https://docs.python.org/3/library/statistics.html

class StandardDeviation():
    @staticmethod
    def standard_deviance(data):
        solution = statistics.stdev(data)
        return solution