from statistics import mode

class Mode():

    @staticmethod
    def mode (data):
        return mode(data)

#ource: https://stackoverflow.com/questions/10797819/finding-the-mode-of-a-list

'''
alternative way to solve: 

from _collections import Counter

def mode (data):
    data = Counter(data)
    mode = data.most_common(1)

    return mode
    
'''